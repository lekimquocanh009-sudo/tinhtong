# Hướng dẫn cộng lô, A/B và đá xiên từ ảnh và TXT theo nhóm và miền

## Xác nhận riêng bảng ba phần Trà Vinh ngày 30/10/2026

- Với bảng ảnh ba phần người dùng gửi ngày 31/10, “2 đài phụ” là **Vĩnh Long và Bình Dương**; không tự áp dụng xác nhận này cho bảng khác.
- Tại cột A của “xỉu chủ 3 đài”, hai ô hiển thị **10** và **30** được người dùng xác nhận là các số ba chữ số **010** và **030**. Giữ số 0 đầu và dò A ở giải 6. Các khoản này không còn là giả định.

## Câu lệnh dùng lại

Người dùng xác nhận ngày 28/10/2026: **“hãy tính tiền”** là câu lệnh yêu cầu tự đọc lại ảnh và TXT của từng nhóm hiện có trong thư mục này, tính theo các quy tắc đã chốt, **dò số trúng luôn** và **xuất Excel theo mẫu đã dùng với đầy đủ kết quả trúng**. Không cần đợi yêu cầu dò số hoặc xuất Excel riêng. Quy trình đầy đủ nằm trong `../AGENTS.md`.

- Tự tra kết quả đúng ngày, đúng đài; dò đủ lô, A/B/XC, đá thường/đá thẳng và đá xiên, lưu giải và số làm căn cứ.
- Điền các cột Tr đá, Tr, SL trúng trong Excel. Tr ghi loại/số/đài/mức×lần; SL trúng là tổng mức gốc×số lần về, chưa nhân tỷ lệ trả thưởng.
- Kết quả chưa có hoặc nguồn chưa đọc được thì ghi rõ phần chưa dò; không dùng 0 thay cho chưa có dữ liệu.
- Người dùng cho phép **tạm đọc/tạm tính theo cách hiểu hợp lý khi chưa rõ và tô vàng các điểm đó trong Excel**, kèm ghi chú cách đọc và căn cứ. Tiếp tục tính/dò các khoản này, không chờ xác nhận riêng nếu có thể suy được từ nguồn. Số người dùng đã xác nhận luôn được ưu tiên.

## Nguồn và cách chia kết quả

- Ảnh nằm trong `C:\Users\Admin\Downloads\TinhTongDe\AnhCacNhom`.
- Mỗi thư mục con trực tiếp là một nhóm.
- Đọc cả các file `.txt` trong từng thư mục nhóm, bao gồm `tinnhan.txt`; các khoản đặt bằng chữ được cộng cùng ảnh của đúng nhóm/ngày/miền.
- Giữ giờ gửi, nội dung gốc, đường dẫn TXT và công thức từng khoản để kiểm tra. Tin `[Ảnh]` chỉ là dấu tham chiếu ảnh, không cộng thêm một lần.
- TXT có nhiều lượt xuất: chỉ loại bản tin trùng có cùng giờ, người gửi và nội dung giữa các lượt xuất; không bỏ các khoản khác nhau chỉ vì trùng số hoặc trùng giờ.
- Đối chiếu nội dung TXT với ảnh chụp tin nhắn để tránh cộng lại cùng một khoản khi có bằng chứng. Không tự coi các khoản cùng số là trùng.
- Tin không đọc được, nhãn dán, tin trò chuyện và khoản chưa rõ phải ghi riêng; không suy ra tiền từ giờ gửi hay tổng ghi sẵn. Báo rõ tổng tạm tính khi nguồn chưa đầy đủ.
- Trong mỗi nhóm, tách riêng miền Nam, miền Trung, miền Bắc; xác định theo ký hiệu miền/đài trên phiếu.
- Mỗi ảnh ghi một dòng; ảnh chỉ có đá xiên vẫn giữ đúng nhóm/miền.
- Bảng gồm: nhóm, miền, số ảnh, lô trực tiếp, đá thường quy ra lô, tổng lô, A, B, AB, tổng lô + AB, đá xiên riêng.

## Quy tắc người dùng đã xác nhận

1. **Lô 1k = 1 đơn vị**; không nhân hệ số thu tiền 15/23.
2. **Đá thường 1n = 2 lô cho một cặp ở một đài**. Cộng kết quả quy đổi vào cột lô.
3. **Luôn có hai cột ĐX 2đ và ĐX 3đ trong bảng tổng theo nhóm, theo miền và tổng chung**, kể cả kết quả trả lời trong chat. Miền không có thì ghi 0. Giữ cột riêng theo mức ghi mỗi cặp, chưa nhân hệ số quy đổi đài và chưa gộp vào lô/AB.
4. **Miền Bắc: A ×4, B ×1; AB1 = 5 đơn vị**. AB2 = 10 đơn vị cho mỗi số.
5. Miền Nam/Trung dùng mức A/B ghi trên phiếu: A5 = 5, B5 = 5, AB5 = 10 mỗi số mỗi đài.
6. Người dùng định nghĩa A là số xổ đầu tiên của giải 8 mỗi đài; B là số xổ cuối cùng của giải đặc biệt. Giữ nguyên cách gọi của người dùng; quy đổi miền Bắc theo hệ số được xác nhận ở trên.
7. Cộng đủ số lượng số và số đài áp dụng của từng khoản.
8. Tổng khoanh là tham khảo, không dùng suy ra mức lô hoặc tiền đá.
9. Người dùng đã xác nhận đá vòng tất cả cặp: nhóm n số có n×(n−1)/2 cặp; nhóm 4 số = 6 cặp, nhóm 3 số = 3 cặp. Đá thường sau đó nhân mức đá × số đài ×2 để cộng vào lô.
10. Khi thư mục nhóm thay đổi, kiểm kê lại tên nhóm và ngày ảnh; không dùng tên nhóm hoặc kết quả cũ thay cho nhóm hiện có.
11. Người dùng xác nhận ngày 28/10/2026 cho bộ tin ngày 27/10/2026: **qua 17:30 là tính miền Bắc hết**, kể cả tin không ghi miền. Quy tắc này chỉ xác định miền, không tự giải nghĩa các ký hiệu còn mơ hồ.
12. Người dùng xác nhận **hàng 1 = 10–19**, **hàng 2 = 20–29**, mỗi hàng đủ 10 số. Không dùng quy tắc này để thay đổi phiếu “hàng 10” đã được xác nhận riêng trước đó.
13. **XC là cách gọi khác của AB**. Ví dụ 588,811,665 XC5 BT+VT = 3 số × (A5 + B5) × 2 đài = 60 A/B.
14. Bỏ các tin không liên quan tới Lô, A/B, XC, đá xiên, đá thẳng, gồm các tin “9”, “1th hoi” trong bộ TXT hiện tại. Tin bị mất nội dung không được tự phân loại là không liên quan; vẫn ghi số lượng nguồn chưa đọc được.
15. **Xác nhận sửa ngày 29/10/2026 ưu tiên bản hiểu cũ: AB3 số chỉ miền Bắc A×3, B×1; miền Nam/Trung A×1, B×1.** A dò ba số cuối giải6, B dò ba số cuối đặc biệt. Ví dụ Nam361 AB25 =25+25=50; Bắc691 AB10 =10×3+10=40. Mỗi giải A/B trúng cộng mức gốc, không nhân lại hệ số ghi.
16. **Điểm không rõ được tạm tính theo cách hiểu hợp lý và tô vàng**: lưu trường chưa chắc, cách hiểu chọn và căn cứ. Tô vàng ô đầu vào và kết quả chịu ảnh hưởng ở bảng tổng/chi tiết trúng, thêm chú giải “Ô vàng = tạm đọc/tính theo ngữ cảnh”. Các dòng hoàn toàn không có nội dung để suy ra số/mức được tô vàng và ghi chưa tính được, không tự bịa khoản đặt. Không đánh dấu một cách đọc đã được người dùng xác nhận là còn nghi vấn.

## Xác nhận từ bảng chuẩn Hạ ngày 29/10/2026

- **Đài chính/phụ thứ Năm:** theo quy ước người dùng, An Giang là đài chính; **2ĐP = Tây Ninh + Bình Thuận**. Không suy đài chính theo thứ tự hiển thị trên trang kết quả. Bỏ đánh dấu giả định ở các khoản 2ĐP đã được xác nhận.
- **Đá thường:** số cặp trúng tại một đài = **min(số lần về con thứ nhất, số lần về con thứ hai)**. Bắc52–49 đá2, mỗi con về2 lần =>2 cặp × mức2 =4. Không chặn một cặp tối đa1 lần và không lấy tích2×2 thành4 cặp. Một con về1 lần, con kia về2 lần thì vẫn chỉ1 cặp. Giữ từng lần ghép và giải đối chiếu, không tái dùng một lần về cho nhiều cặp cùng số.
- Trung TT10, ảnh16:58:38: **Quảng Bình57–75 đá thường1**, không phải Quảng Trị + Quảng Bình ĐX1. Dòng này L32, bỏ ĐX2đ1; tổng Trung L438, ĐX2đ0, ĐX3đ1.
- Bắc TT11, ảnh17:49:20: 52 về G4 4352 và G5 2452;49 về G5 7149 và G7 49. Tr đá4, tổng Bắc Tr đá7.
- Nam khớp bảng chuẩn: A/B2306 L530 ĐX2đ5 ĐX3đ2 Tr65. Trung A/B750 L438 Tr33. Bắc A/B843 L227 Tr108.
- Tổng ghi5094, ĐX2đ5, ĐX3đ3; Lô/A/B trúng206, đá trúng riêng7. Bản trước5092/ĐX2đ6/đá trúng5 đã sửa. Sửa file phân tích ảnh rồi đọc lại cả hai file để tính; không dùng tổng chuẩn thay nguồn.

## Số bị gạch X trên phiếu

- Người dùng xác nhận ngày30/10/2026: **gạch X có nghĩa xóa số đó, không tính số bị xóa**. Không đọc nét gạch thành phần của chữ số hoặc giữ số đó vì vẫn nhìn thấy bên dưới.
- Với đá/ĐX, loại số bị xóa rồi tạo lại các cặp từ số còn hiệu lực. Bỏ cả phần ghi và phần trúng của mọi cặp chứa số đã xóa. Ghi số đã xóa cùng căn cứ trong bản phân tích; xác nhận người dùng không còn là ô tạm đọc.
- Vĩnh An12 ảnh29/10 lúc16:09:51, ANH-03: cụm cuối90,82,92 ĐX1, số82 bị gạch X => **chỉ còn90–92 ĐX1**. Toàn phiếu:90–91 ĐX2 +91–92 ĐX2 +90–92 ĐX1 = **ĐX2đ5, ĐX3đ0**, không có trúng đá. Bỏ cách tính cũ7 điểm và khoản trúng82–92 mức2 đã cộng nhầm.
- Tổng nhóm sau sửa: Lô1755, A/B3515, tổng ghi5270; ĐX2đ16, ĐX3đ0; Lô trúng553, A/B0, đá thường trúng15, ĐX trúng0. Những giả định khác về mức lô/đài/tin hủy giữ riêng.

## Tin nhắn hủy khoản đặt

- Người dùng xác nhận: người nhắn kêu bỏ thì bỏ khoản đó, không giữ nguyên khoản đã được yêu cầu hủy trong tổng.
- Đối chiếu ảnh/tin được trích để loại đúng khoản. Nếu bản xuất chỉ còn nhãn hình ảnh, phải ghi rõ cách ghép tạm theo ngữ cảnh và tô vàng phần nguồn bị loại cùng tổng ghi/trúng chịu ảnh hưởng; không nhận là người dùng đã xác nhận mã ảnh khi họ chỉ xác nhận ý định hủy.
- Riêng Vĩnh An12 nguồn29/10, tin17:09:13: tạm gắn với ảnh gần nhất17:08:33, phiếu25,24,35,64,65,85 AB10/lô5 ba đài Trung. Đây là ghép tạm của trợ lý, không phải quy tắc luôn hủy ảnh gần nhất cho mọi trường hợp.

## Công thức

```text
Lô trực tiếp = số lượng số × mức lô × số đài
Đá thường quy ra lô = số cặp × mức đá × số đài × 2
Tổng lô = lô trực tiếp + đá thường quy ra lô

Nam/Trung:
A = số lượng số × mức A × số đài
B = số lượng số × mức B × số đài

Bắc:
A = số lượng số × mức A × 4
B = số lượng số × mức B
AB = A + B

Tổng lô + AB = tổng lô + A + B

AB 3 số:
A Nam/Trung = số lượng số × mức A × số đài
A Bắc = số lượng số × mức A × 3
B = số lượng số × mức B × số đài
Dò A: 3 số cuối từng số giải 6; dò B: 3 số cuối giải đặc biệt.
```

Ví dụ ảnh Chị Chín 18-03-24: 13 số lô 2 = 26; hai cặp đá 1n = 2 × 1 × 2 = 4 lô; tổng lô ảnh = **30**.

## Cột đá xiên

**Sửa ngày30/10:** ví dụ82–92 ở dưới chỉ minh họa quy tắc ghép nếu cặp còn hiệu lực. Trong ảnhANH-03 của Vĩnh An12, người dùng đã xác nhận82 gạch X là xóa; cặp82–92 không được ghi hoặc tính trúng thực tế.

- Xác nhận mới của người dùng khi tính Vĩnh An12 ngày29/10: **cặp82–92 ĐX1 An Giang+Bình Thuận, cảhai số về ở cảhai đài, chỉ trúng2 điểm**. Trong cùng một cặp đặt, mỗi lần về chỉ ghép một lần; không tính bốn tổ hợp đài. ĐX được ghép cùng hoặc chéo trong phạm vi đài chọn; số cặp ghép = min(tổng số lần về từng con trong phạm vi). Mỗi cặp đặt riêng có lượt ghép riêng.

- Ghi riêng số cặp, mức đá và tên/số đài.
- Bảng hiện cộng **mức ghi mỗi cặp**: số cặp × mức ghi, chưa quy đổi theo số đài/cặp đài.
- Ví dụ 3 cặp đá xiên 1n TP+ĐT: ghi 3 cặp, mức 1n, phạm vi TP+ĐT; tổng mức ghi = 3.
- Không gộp đá xiên vào lô hoặc tổng lô + AB.
- Nếu cần quy đổi đá xiên theo số cặp đài, phải dùng quy tắc do người dùng cung cấp, không tự suy hệ số.
- Bảng chi tiết giữ tên/số đài để tính lại khi có quy tắc.
- Xác nhận qua bảng chuẩn Vĩnh An ngày29/10: ĐX2đ được tính cặp cùng một đài trong phạm vi chọn, ví dụ86–54 đều về Đồng Nai vẫn trúng. Đếm cặp trúng, không lấy số lần về từng con nhân với nhau. Cặp52–57 mức3 chỉ trúng3 dù57 về2 lần; đá75–05 mức2 chỉ tính2. Một đài có hai cặp trúng thì tính cảhai cặp. Giữ căn cứ đài/giải cho mỗi cặp.

## Xác nhận riêng cho bộ ngày 28/10/2026

- Nhóm Hạ: tin 17:40:55 “Mb 74 lô 20đ” và tin 17:41:06 “20đ lô 74 mb nha b” là **hai khoản đặt riêng**, người dùng xác nhận cộng **40 lô**. Không loại bản tin thứ hai là nhắc lại.
- Nhóm Phú Quý: hai ảnh sổ lúc 16:15:40 và 17:14:06 người dùng xác nhận **lô 5k mỗi số**. Bản tính áp dụng ảnh 16:15 miền Nam 3 đài và ảnh 17:14 miền Trung 2 đài theo phần tin trước/sau; lưu rõ căn cứ này trong báo cáo. Giữ dòng số lặp trên sổ là khoản riêng.
- Sửa bản đọc ảnh Phú Quý **16:15:40**: dòng gần cuối cột trái là **19**, trước đó đọc nhầm thành 79. Dãy cột trái là **79,97,07,70,27,72,77,80,19,97**; cột phải **18,92,25,65,23,32,33,87,78,56**. Vẫn 20 dòng, tổng ghi 300 lô. Khoản 19 lô5 trúng Đồng Nai (ĐB 220019) và Sóc Trăng (G1 40919), cộng thêm 10 lô trúng cho ảnh này.
- Sửa bản đọc ảnh Phú Quý **17:14:06**: người dùng xác nhận dòng đầu cột trái là **19**, không phải 78. Danh sách đúng: **19,97,89,98,32,23,45,54,17,71,25,50,58,85,86,68**. Vẫn 16 số, lô5 ở 2 đài Trung = 160 lô. 19 không trúng hai đài Trung ngày 28/10; bỏ 5 lô trúng nhầm của 78 Đà Nẵng. Ảnh này trúng 98,17,86 Khánh Hòa, tổng 15; tổng lô trúng Phú Quý sau cả hai sửa là **125** (Nam 60, Trung 35, Bắc 30).
- Bảng mẫu phải thêm đủ dòng khi một miền có hơn 25 nguồn đặt; không bỏ bớt ảnh/tin để vừa mẫu.

## Phiếu đã sửa cách đọc

### Hai ảnh Nguyen Thanh Tra ngày 28/10/2026

- Người dùng xác nhận ngày của hai ảnh đính kèm là **28/10/2026**.
- Người dùng sửa rõ: **số cuối của mỗi tin là mức điểm của mỗi con**. Ví dụ cuối tin 30k thì mỗi số phía trước đánh lô 30 điểm; 20k=20; 46k=46; 92k=92; 184k=184 điểm/con. Không thêm 30/20/46/92/184 vào dãy số đánh.
- **Không chia 23, không tính giá tiền** trong lần tính lại này. Cách quy đổi tiền của bản trước đã bị thay thế bởi lời sửa trực tiếp trên. Tổng ghi tính bằng điểm, phần trúng = mức điểm × số lần về.
- Tin Nam ghi rõ 2 đài ĐN + CT. Tin Trung ghi 2 đài, tạm đối chiếu Đà Nẵng + Khánh Hòa theo ngày và tô vàng tên đài/kết quả liên quan.
- Chỉ tính 10 tin trong hai ảnh này; không cộng thêm tổng Hạ hoặc Phú Quý. Mức cuối tin áp dụng cho mỗi số, mỗi đài, có ghi rõ trong Excel.

Phương Vân, ảnh 15-48-57 (phiếu miền Nam số 10):

- Chữ viết là **“hàng 10 A5k”**.
- Gồm **11,12,13,14,15,16,17,18,19**: 9 số, không có 20.
- Khoản này riêng với 5 số AB5 bên cạnh.
- 5 số AB5 = 50 đơn vị; hàng 10 A5k = 9 × 5 = 45 đơn vị.
- Theo bố cục ảnh, đang áp dụng ĐT cho cả hai khoản: **AB = 95**.
- Ba cặp đá xiên TP+ĐT đưa cột riêng.

## Quy trình

**Quy trình mới được người dùng chốt ngày 29/10/2026: làm xong và lưu từng bước, sau đó mới tính tổng từ hai file.** Áp dụng riêng cho từng nhóm và từng ngày, không trộn nhiều ngày.

### Bước 1 — Phân tích ảnh và ghi thành một file

- Kiểm kê tất cả ảnh thực tế, ghi tên file, SHA-256, ngày/giờ và mã nguồn. File `bao-cao*.json` chỉ là nhật ký tải.
- Đọc hết từng ảnh; phóng to chỗ mờ, phân biệt chữ mặt sau và số bị gạch. Đọc phạm vi mức ghi chung cho cả nhóm số trước khi tách khoản; không gán mỗi dòng một loại.
- Ghi từng số/cặp, loại Lô/A/B/AB/XC/đá, mức gốc, miền, tên/số đài và hệ số áp dụng. Giữ các dòng đặt lặp riêng, không chỉ ghi tổng ảnh.
- Ghi cả ảnh tổng/biên nhận bị loại, ảnh trùng có bằng chứng, chỗ tạm đọc và phần hoàn toàn không đọc được, cùng lý do.
- Lưu thành **một file** `AnhCacNhom/PHAN_TICH_ANH_<nhom>_<ngay>.json`, rồi kiểm tra file đã lưu trước khi sang bước 2. Giữ nguyên ảnh nguồn.

### Bước 2 — Phân tích tin nhắn TXT và ghi thành một file riêng

- Đọc toàn bộ TXT đang tồn tại, gồm mọi lượt xuất. Giữ giờ gửi, người gửi nếu có và nguyên văn nội dung từng tin.
- Tách từng khoản đặt thành số/cặp, mức gốc, loại, miền và đài. Ghi rõ giả định nếu suy từ tin trước/sau.
- Đánh dấu riêng tin `[Ảnh]`, nhãn dán, trò chuyện, thu hồi, tin trích lại, bản xuất trùng và tin không đọc được. Thiếu nội dung không đồng nghĩa không liên quan.
- Đối chiếu với file phân tích ảnh ở bước 1. Khoản có bằng chứng trùng ảnh phải ghi `duplicate_of` trỏ về mã nguồn ảnh và nêu bằng chứng; không tự xóa khoản vì cùng số hoặc cùng giờ.
- Lưu thành **một file khác** `AnhCacNhom/PHAN_TICH_TXT_<nhom>_<ngay>.json`, rồi kiểm tra file đã lưu. Giữ nguyên TXT nguồn.

### Nội dung tối thiểu của hai file phân tích

- Thông tin nhóm, ngày dữ liệu, loại nguồn và kiểm kê tên file/hash hiện tại.
- `records`: mã khoản duy nhất, mã/đường dẫn nguồn, ngày/giờ, nội dung đọc được hoặc nguyên văn tin, số/cặp, loại, mức ghi gốc, phạm vi mức chung, miền/đài, hệ số và phép tính thành phần.
- `assumed_fields` và ghi chú: trường nào tạm hiểu, cách đọc chọn và căn cứ; phân biệt với xác nhận trực tiếp của người dùng.
- `skipped`, `duplicates`, `pending`: nguồn không cộng, bằng chứng trùng và nội dung còn thiếu. Mỗi ảnh/tin trong kiểm kê phải có trạng thái xử lý.
- Dùng JSON UTF-8 trình bày có xuống dòng; số đánh lưu dạng chuỗi, ví dụ `"04"`, để giữ số 0 đầu.
- Không có ảnh hoặc không có TXT vẫn lưu file tương ứng ghi rõ không có nguồn. Nếu nguồn lỗi/thiếu nội dung, ghi chưa tính được; không biến thành số 0 hoặc tự tạo khoản đặt.

### Bước 3 — Tính tổng từ cả hai file, dò trúng và xuất Excel

- Đọc lại **cả hai file đã lưu trên đĩa**. Kiểm tra chúng khớp nhóm/ngày và kiểm kê nguồn hiện tại; cập nhật bước phân tích liên quan nếu nguồn đã đổi.
- Chỉ lấy các khoản hợp lệ từ hai file để tính. Đối chiếu trùng giữa ảnh và TXT bằng mã nguồn/bằng chứng; mỗi khoản được cộng đúng một lần.
- Cộng riêng phần ảnh, phần TXT và tổng hai phần theo từng nhóm/ngày/miền. Giữ riêng ĐX 2đ và ĐX 3đ. Không dùng tổng cũ hoặc bản đọc chưa lưu trong bộ nhớ/script để thay thế hai file.
- Mỗi khoản ở bảng tổng và Excel phải truy ngược về mã khoản trong file phân tích ảnh hoặc TXT. Nếu phát hiện đọc sai, sửa file phân tích gốc rồi tính lại từ cả hai file.
- Dò đủ từng số và cặp đúng ngày, miền, đài theo quy tắc đã chốt; lưu giải đối chiếu. Kiểm tra tổng các miền khớp tổng nhóm và tổng hai loại nguồn; giữ riêng phần trúng đá.
- Xuất Excel theo mẫu, điền kết quả trúng, đưa giả định vào đúng ô đầu vào và kết quả tô vàng, ghi rõ phần chưa tính/chưa dò. Kiểm tra công thức và xem ảnh dựng trước khi gửi.






## Phạm vi lượt tính ngày 29/10/2026

- Người dùng xác nhận “hãy tính tiền - những người đã tính” nghĩa là **bỏ qua người đã tính, tính người còn lại**. Không hiểu dấu trừ này thành yêu cầu tính lại các nhóm đã hoàn tất.
- Lượt này bỏ qua Cua, Mén 2, Phú Quý, Riêng 10 và Riêng Lực; kiểm tra nguồn của các nhóm còn lại. Nguồn chỉ có báo lỗi xuất 0 tin và không có ảnh thì ghi chưa tính được, không tự tạo tổng bằng 0.
- Ngày 30/10/2026 người dùng xác nhận: chỉ bỏ Lực của ngày trước đã tính; **Lực ngày mới tính bình thường**, bao gồm dữ liệu 30/10. Không áp dụng danh sách bỏ qua ngày 29/10 cho ngày mới.

## Rà soát Lực ngày 29/10/2026 cho nguồn 28/10/2026

- Người dùng yêu cầu dò kỹ lại sau khi hỏi phần A/B. Đã kiểm lại 3 ảnh sổ, 2 tin đặt và từng giải của 6 đài. A/B Nam trúng 30 điểm: hai khoản 19 B10 Đồng Nai = 20; 59 A10 Cần Thơ = 10. A/B Trung và Bắc đã dò, không trúng.
- Đây là **sửa bản đọc ảnh của trợ lý**, không phải mức mới do người dùng xác nhận: dòng gần cuối cột AB3Đ ảnh Nam 16:10:29 đọc là **19 B10**, bỏ A10 đã cộng trước đó (giảm 30 điểm ghi). Dòng 59 cột ST đọc hợp lý hơn là **A10 B40**, thay B240 (giảm 200 điểm ghi); **B40 vẫn là tạm đọc, giữ vàng**. Không tự trở lại bản đọc cũ khi tái dùng script.
- Kết quả sau rà: Lô 2636, A/B 2275, tổng ghi 4911; ĐX 2đ = 9, ĐX 3đ = 0. Tổng lô + A/B trúng 647 không đổi (Nam 301, Trung 286, Bắc 60); riêng xiên 01–10 miền Trung mức 1 trúng, giữ riêng theo quy tắc chưa nhân thưởng.
- File thay thế là `BANG_LUC_28-10-2026_RA_SOAT.xlsx` trong thư mục outputs của chat. File trước rà còn tổng ghi 5141 là bản cũ.
- Trước khi chốt các lần sau, đối chiếu toàn bộ giải đúng ngày/đài, kiểm tra cả khoản không trúng và cặp đá; đối chiếu tổng tính độc lập với giá trị lưu trong Excel. Hiển thị rõ Lô trúng và A/B trúng riêng theo miền; 0 đã dò khác với chưa dò. Đưa các khoản A/B trúng lên trước trong cột Tr để không bị chìm giữa danh sách lô.

## Mẫu cột người dùng yêu cầu

- Nam/Trung: TT | A | L | ĐX 2đ | ĐX 3đ | Tr đá | Tr | số lượng trúng.
- Bắc: TT | A | L | Tr đá | Tr | số lượng trúng.
- A trong bảng mẫu là tổng A/B đã quy đổi theo miền; L gồm lô trực tiếp và đá thường.
- Tr đá là chỗ ghi cặp đá trúng; Tr là chỗ ghi số/mức trúng, cột bên cạnh là số lượng trúng.
- Nếu chưa dò kết quả, để trống các cột Tr đá/Tr và ghi rõ chưa dò; không điền 0 thay cho chưa có dữ liệu.
- ĐX 2đ và ĐX 3đ giữ mức gốc theo từng cặp. Không gộp hai cột khi tổng hợp.
- Bảng Excel: một sheet mỗi nhóm; ba khối Nam, Trung, Bắc đặt cạnh nhau, chữ tiêu đề đỏ, lưới mảnh, hàng cộng có nền xanh ngọc như ảnh mẫu.

## Vĩnh An, nguồn ngày 28/10/2026

- Người dùng xác nhận ngày 29/10: phiếu lúc 16:06:22, dòng ĐN + ST là **84–91 ĐX3**. Không coi số 91 bên dưới chỉ là khoản lô; giữ cả cặp ĐX và 91 lô20 đã ghi trên phiếu.
- Phiếu Bắc lúc 18:08:09: **86–49–63–97 đá2 là đá vòng 6 cặp**, người dùng xác nhận, không phải một bộ xiên4.
- Tin 17:22:07 trích lại nguyên văn khoản CT lúc 16:00:53 kèm xin ứng40, chỉ tham chiếu, không cộng lặp. Tin thu hồi không đủ căn cứ tự xóa một phiếu đặt khác.
- Lượt tính riêng này không bật lại lịch theo dõi; người dùng đã yêu cầu dừng trước đó.
- Bảng chuẩn người dùng29/10 sửa cách đọc mức chung: NamTT17 cả21,44 cùngAB50 vàlô10; NamTT21 cả09,49,89,80,40 cùnglô5 vàAB10; NamTT23 cả84,91 cùnglô20; TrungTT9 cả55,56 cùngA10B5; TrungTT15 cả49,80,25,35 cùngAB20 vàlô20.
- Hai tin G a c90 vàG a c02_49 là lô theo bảng chuẩn, không phảiA. NamTT25 là39,93, không phải59,95. BắcTT15 số đầu88, không phải86. Nam361AB25=50 theo quy tắc NamA×1B×1 mới xác nhận, không là ngoại lệ phiếu.
- Kết quả khớp bảng chuẩn: NamA3375 L1009 ĐX2đ14 Trđá2 Tr617; TrungA680 L598 ĐX2đ16 Trđá3 Tr45; BắcA365 L549 Trđá10 Tr123. Tổng ghi6576, ĐX2đ30, ĐX3đ0; lô/A/B trúng785, mức đá trúng riêng15. Bản trước5951/760 đã bị thay thế.
