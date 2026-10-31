# Hướng dẫn tính tổng và dò số trúng

Tài liệu và quy tắc đã được xác nhận, cập nhật ngày **31/10/2026**.

## Đọc hướng dẫn

- [Hướng dẫn tính tổng từ ảnh và TXT](AnhCacNhom/HUONG_DAN_TINH_TONG.md): cách đọc phiếu, cộng điểm, xác định miền/đài, dò trúng và trình bày Excel.
- [Quy ước thực hiện công việc](AGENTS.md): quy trình cho câu lệnh “hãy tính tiền”, kiểm tra nguồn và kết quả trước khi xuất file.

## Đối chiếu ảnh từng dòng

[prepare_image_review.py](prepare_image_review.py) tạo ảnh cắt theo cột/dòng, phóng màu gốc và bản xám cân tương phản để đọc kiểm lại. Công cụ giữ nguyên ảnh nguồn, lưu SHA-256 và tọa độ trong `manifest.json`; không OCR hoặc tự chốt số.

Yêu cầu Python và Pillow. Ví dụ sử dụng:

```bash
python prepare_image_review.py --source duong-dan-anh.png --layout layout.json
```

Layout khai báo kích thước ảnh sau khi xoay theo EXIF, khung từng cột và khoảng trên/dưới của từng dòng. [Layout mẫu Lực](image_review_layout_luc30.json) chỉ dành cho ảnh cắt kích thước525×1185; với ảnh khác phải kiểm tra và đặt lại tọa độ. Công cụ từ chối layout có kích thước không khớp hoặc khung nằm ngoài ảnh.

Đọc lần đầu trước khi xem kết quả xổ số, rồi rà lại ảnh cắt và cách viết chữ số trên cùng phiếu. Trước khi xuất Excel, đối chiếu từng khoản trúng về đúng số, mức, loại và đài. Tổng ghi khớp không bảo đảm chữ số đã đọc đúng; phần chưa chắc vẫn ghi rõ và tô vàng theo hướng dẫn.

## Các điểm đã chốt

- Thực hiện tuần tự: phân tích ảnh và lưu một file JSON; phân tích TXT và lưu một file JSON khác; đọc lại cả hai file để tính tổng, dò trúng và xuất Excel. Tách riêng từng nhóm, ngày và miền.
- Lô 1k/1n = 1 điểm. Chỉ quy tiền hoặc thưởng khi có hệ số được người dùng xác nhận.
- A/B 2 số miền Nam/Trung: A ×1, B ×1. Miền Bắc: A ×4, B ×1.
- A/B 3 số miền Nam/Trung: A ×1, B ×1. **Chỉ miền Bắc A ×3, B ×1.**
- Đọc mức chung cho toàn bộ nhóm số trước khi tách khoản; không tự gán mỗi dòng một loại.
- Đá thường quy về lô; ĐX 2đ và ĐX 3đ giữ riêng. Đá thường trúng trong một đài: số cặp = min(số lần về mỗi con). Hai con đều về hai lần thì có hai cặp trúng, không lấy tích thành bốn cặp.
- Theo quy ước người dùng, thứ Năm An Giang là đài chính; **2ĐP = Tây Ninh + Bình Thuận**.
- Số bị gạch X là số đã xóa: bỏ phần ghi, phần trúng và mọi cặp chứa số đó. Tin nhắn yêu cầu hủy phải đối chiếu để bỏ đúng khoản.
- ĐX được ghép trong phạm vi các đài đã chọn, gồm cùng đài và chéo đài; mỗi lần về của một số chỉ dùng một lần trong cùng cặp đặt, không nhân các tổ hợp đài.
- Danh sách người đã tính chỉ áp dụng đúng đợt/ngày. Lực ngày mới được tính bình thường theo xác nhận ngày 30/10.
- Phần tạm đọc được tô vàng ở đầu vào và kết quả chịu ảnh hưởng. Nội dung hoàn toàn thiếu thì ghi chưa tính được.
- Câu lệnh **“hãy tính tiền”** bao gồm tính tổng, dò số trúng và xuất Excel đã điền kết quả.

Ảnh/TXT đầu vào và Excel kết quả được giữ ở máy làm việc. Repo lưu hướng dẫn cùng công cụ đối chiếu ảnh; lịch tự theo dõi thư mục hiện đã tắt theo yêu cầu người dùng.
