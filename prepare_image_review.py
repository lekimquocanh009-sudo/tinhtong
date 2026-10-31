"""Tạo ảnh đối chiếu từng dòng; không nhận dạng hoặc tự sửa chữ số.

Ví dụ:
  python prepare_image_review.py --source outputs/luc_30/0.png \
    --layout image_review_layout_luc30.json

Tọa độ layout dùng ảnh sau khi áp dụng hướng EXIF. Mỗi cột giữ nhãn riêng;
mỗi dòng có ảnh phóng to màu gốc và ảnh xám cân tương phản để so sánh.
"""
import argparse
import hashlib
import json
import math
import pathlib
import re
import sys
from PIL import Image, ImageOps, ImageDraw

ROOT=pathlib.Path(__file__).resolve().parent

def slug(value):
    return re.sub(r'[^a-zA-Z0-9_-]+','_',str(value)).strip('_') or 'column'

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',required=True,type=pathlib.Path)
    parser.add_argument('--layout',required=True,type=pathlib.Path)
    parser.add_argument('--out',type=pathlib.Path)
    args=parser.parse_args()
    source=args.source.resolve()
    source_bytes=source.read_bytes()
    source_hash=hashlib.sha256(source_bytes).hexdigest()
    layout_bytes=args.layout.read_bytes()
    layout=json.loads(layout_bytes.decode('utf-8-sig'))
    scale=layout.get('scale',4)
    if not isinstance(scale,int) or not 1<=scale<=6:raise ValueError('scale phải là số nguyên1–6.')
    rows_per_page=layout.get('rows_per_page',6)
    if not isinstance(rows_per_page,int) or not 1<=rows_per_page<=12:raise ValueError('rows_per_page phải là số nguyên1–12.')
    with Image.open(source) as original:
        source_size=list(original.size)
        frame=ImageOps.exif_transpose(original).convert('RGB')
    width,height=frame.size
    if layout.get('oriented_size')!=[width,height]:raise ValueError('Kích thước ảnh khác layout; phải kiểm lại tọa độ, không tự dùng layout của ảnh khác.')
    output=(args.out or ROOT/'outputs/image_review'/source_hash[:12]).resolve()
    try:output.relative_to(ROOT.resolve())
    except ValueError:raise ValueError('Thư mục đầu ra phải nằm trong workspace dự án.')
    output.mkdir(parents=True,exist_ok=True)
    manifest={'source_file':str(source),'source_sha256':source_hash,'source_size':source_size,
              'oriented_size':[width,height],'layout_file':str(args.layout.resolve()),
              'layout_sha256':hashlib.sha256(layout_bytes).hexdigest(),
              'method':'Cắt đúng tọa độ, phóng bằng LANCZOS. Giữ song song màu gốc và xám autocontrast cutoff1%. Không OCR, không vẽ/sửa nét chữ.',
              'status':'prepared_for_visual_review','rows':[],'pages':[]}
    frame.save(output/'source_view.png')
    manifest['source_view']=str(output/'source_view.png')
    for column in layout['columns']:
        name=slug(column['id']);x0,y0,x1,y1=column['box']
        if not (0<=x0<x1<=width and 0<=y0<y1<=height):raise ValueError(f'Khung cột ngoài ảnh: {name}')
        crops=[]
        for idx,bounds in enumerate(column['rows'],1):
            top,bottom=bounds
            if not (y0<=top<bottom<=y1):raise ValueError(f'Khung dòng ngoài cột: {name}/{idx}')
            crop=frame.crop((x0,top,x1,bottom))
            grey=ImageOps.autocontrast(ImageOps.grayscale(crop),cutoff=1)
            size=(crop.width*scale,crop.height*scale)
            enlarged=crop.resize(size,Image.Resampling.LANCZOS)
            contrast=grey.resize(size,Image.Resampling.LANCZOS).convert('RGB')
            token=f'{name}_row_{idx:02}'
            paths={}
            for label,img in [('original_crop',crop),('enlarged_color',enlarged),('grey_contrast',contrast)]:
                p=output/(token+'_'+label+'.png');img.save(p);paths[label]=str(p)
            manifest['rows'].append({'id':f'{name}:row:{idx:02}','column':column['id'],'row':idx,
                                     'source_box':[x0,top,x1,bottom],**paths,
                                     'first_read':None,'second_read':None,'resolved_read':None,
                                     'reading_note':None,'status':'needs_visual_read'})
            crops.append((idx,enlarged,contrast))
        for page in range(math.ceil(len(crops)/rows_per_page)):
            selected=crops[page*rows_per_page:(page+1)*rows_per_page]
            cell_width=max(c[1].width for c in selected)
            cell_height=max(c[1].height for c in selected)
            canvas=Image.new('RGB',(2*cell_width+36,len(selected)*(cell_height+32)+42),'white')
            draw=ImageDraw.Draw(canvas)
            draw.text((10,8),f'{name} | Color crop / Grey contrast | source SHA256 {source_hash[:12]}',fill='black')
            for k,(idx,color,grey) in enumerate(selected):
                y=42+k*(cell_height+32)
                draw.text((10,y),f'{name} row {idx:02} | color',fill='black')
                draw.text((cell_width+26,y),f'{name} row {idx:02} | grey contrast',fill='black')
                canvas.paste(color,(10,y+19));canvas.paste(grey,(cell_width+26,y+19))
            p=output/f'{name}_page_{page+1:02}.png';canvas.save(p)
            manifest['pages'].append({'column':column['id'],'page':page+1,'path':str(p),'rows':[c[0] for c in selected]})
    # Bảo đảm công cụ không làm thay đổi tệp nguồn.
    assert hashlib.sha256(source.read_bytes()).hexdigest()==source_hash
    manifest_path=output/'manifest.json'
    manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'manifest':str(manifest_path),'rows':len(manifest['rows']),'pages':len(manifest['pages']),'source_unchanged':True},ensure_ascii=False))

if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
