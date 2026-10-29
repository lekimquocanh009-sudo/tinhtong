# Quy ước làm việc trong TinhTongDe

## Câu lệnh “hãy tính tiền”

Khi người dùng nhắn **“hãy tính tiền”** (không phân biệt hoa/thường, có thể có dấu ngoặc), hiểu là yêu cầu thực hiện ngay toàn bộ quy trình **đọc nguồn → tính tổng → dò số trúng → xuất Excel đã điền kết quả** trong dự án này. Người dùng đã xác nhận lệnh này bao gồm dò số trúng, không chờ nhắc dò riêng. Không chỉ giải thích cách làm hoặc hỏi lại có muốn bắt đầu hay không.

1. Đọc `AnhCacNhom/HUONG_DAN_TINH_TONG.md` để áp dụng các quy tắc người dùng đã xác nhận.
2. Kiểm kê lại từng thư mục nhóm, ngày dữ liệu, toàn bộ ảnh và TXT đang tồn tại trong `AnhCacNhom`. Đọc các nguồn hiện có; không lấy tổng hoặc tên nhóm của lần trước làm dữ liệu mới. Nếu có nhiều ngày, tách riêng từng ngày, không cộng lẫn ngày. Trước khi cộng tổng, bắt buộc lưu riêng bản phân tích ảnh và bản phân tích TXT theo quy trình ba bước dưới đây.
3. Tính từng khoản Lô, A, B, AB/XC, đá xiên, đá thường/đá thẳng. Cộng đúng số lượng số, cặp và đài. Hàng 1 = 10–19; hàng 2 = 20–29; XC = AB. Áp dụng hệ số theo miền và các quy tắc khác trong hướng dẫn, không tự thêm hệ số thu tiền/trả thưởng.
   AB 3 số: theo xác nhận sửa ngày 29/10/2026, **chỉ miền Bắc A ×3, B ×1; miền Nam/Trung A ×1, B ×1**. Dò A ba số cuối giải6, B ba số cuối đặc biệt. Không áp dụng A×4 của Bắc 2 số cho Bắc3 số. Lô/A/B giữ mức gốc khi tính trúng; đá tính theo từng cặp trúng, không lấy tích số lần về hai con.
4. Bỏ tin không liên quan tới các loại trên. Loại bản xuất trùng có bằng chứng; tin `[Ảnh]` chỉ tham chiếu ảnh, không tính thêm. Không tự xóa khoản chỉ vì trùng số hoặc trùng giờ.
5. **Người dùng đã cho phép tạm tính theo cách hiểu hợp lý và tô vàng các điểm chưa rõ.** Có ảnh thì phóng to kiểm tra trước; nếu vẫn mơ hồ, chọn cách đọc có căn cứ từ nét chữ, các dòng trước/sau, miền/đài và quy tắc đã chốt, tiếp tục tính và dò, không dừng để hỏi lại với các khoản có thể suy được. Đánh dấu giả định riêng từng khoản: phần nào tạm đọc (số, mức, loại, miền, đài), cách hiểu đã chọn và căn cứ. **Tô vàng chính ô nguồn/đầu vào chưa chắc cùng ô tổng ghi hoặc trúng chịu ảnh hưởng trong Excel**, kèm ghi chú rõ ràng; không chỉ tô tiêu đề hoặc ghi trong chat. Xác nhận trực tiếp của người dùng luôn ưu tiên hơn suy đoán, không tự đổi lại số đã được sửa. Tin TXT chỉ có dòng “không đọc được nội dung” và không có ảnh/ngữ cảnh đủ để suy ra số, mức thì ghi **chưa đọc/xuất được nội dung, chưa tính được**, tô vàng dòng đó, không tạo số tiền không có căn cứ và không tự coi là tin không liên quan.
6. Lưu chi tiết từng khoản, nguồn, công thức và bảng tổng theo nhóm/miền trong `AnhCacNhom`. Kiểm tra tổng các miền khớp tổng nhóm và tổng chung; không ghi đè ảnh/TXT nguồn.
7. **Tự dò số trúng cho tất cả nhóm**: tra bảng kết quả đầy đủ trên mạng đúng ngày, đúng miền và đài của từng khoản, lưu nguồn đối chiếu. Lô dò đúng số chữ số trên tất cả giải, cộng đủ số lần về; A/B 2 số dò theo quy tắc miền, A/B 3 số dò giải 6/đặc biệt như trên. Dò cả đá thường/đá thẳng và đá xiên, giữ cặp, mức gốc, đài và giải làm căn cứ. Phần trúng = mức ghi gốc × số lần về; chưa có tỷ lệ trả thưởng thì không tự quy tiền thưởng. Nếu kết quả chưa có hoặc nguồn thiếu, ghi rõ khoản nào chưa dò, không coi là không trúng.
   Riêng đá: đếm cặp trúng theo phạm vi đài, không nhân số lần về từng con với nhau. Bảng chuẩn Vĩnh An xác nhận ĐX2đ tính cả cặp86–54 cùng về Đồng Nai. Một mức ghi sau dấu gạch/ngoặc có thể áp dụng toàn bộ nhóm số cho nhiều loại, phải đọc cả nhóm trước khi tách khoản; không tự gán mỗi dòng một loại.
8. **Tự xuất Excel theo mẫu đã chốt và điền phần trúng**, không chờ người dùng nhắc thêm: mỗi nhóm một sheet, ba khối Nam–Trung–Bắc cạnh nhau; tiêu đề đỏ, lưới mảnh, hàng xanh ngọc. Nam/Trung có TT | A | L | ĐX 2đ | ĐX 3đ | Tr đá | Tr | SL trúng; Bắc có TT | A | L | Tr đá | Tr | SL trúng. A trong mẫu là tổng A/B, L đã gồm đá thường. Giữ riêng hai cột ĐX 2đ/3đ trong mọi bảng tổng. Điền Tr đá (cặp/mức), Tr (loại/số/đài/mức×lần) và SL trúng (tổng mức×lần, chưa nhân thưởng); có chi tiết giải đối chiếu ở dưới. Chỉ ghi chưa dò/để trống phần trúng khi thực sự chưa có dữ liệu kết quả hoặc chưa đọc được nguồn.
9. Dùng kỹ năng Spreadsheets khi tạo/sửa Excel; kiểm tra công thức, tổng trúng theo nhóm/miền và xem ảnh dựng của từng sheet trước khi giao file. Nếu file cũ bị khóa, lưu một bản mới có tên rõ ràng, không đóng ứng dụng của người dùng.
10. Trả lời ngắn bằng tiếng Việt, kèm tổng ghi, tổng trúng từng nhóm và file Excel đã dò. Nhắc các ô vàng là phần tạm hiểu để người dùng kiểm tra; nêu ngắn phần nguồn/kết quả chưa đọc được nếu có.

Các script `calc_txt27.mjs`, `build_txt27_excel.mjs` và các script ngày khác là công cụ cho bộ nguồn đã đọc ở lần trước. Trước khi tái sử dụng, kiểm tra và cập nhật bản đọc cho nguồn/ngày thực tế; không chạy nguyên dữ liệu cũ rồi nhận là đã đọc bộ mới.

Lưu quy tắc mới người dùng xác nhận vào `AnhCacNhom/HUONG_DAN_TINH_TONG.md` để dùng cho lần tiếp theo. Phân biệt quy tắc chung với ngoại lệ chỉ áp dụng cho một phiếu/ngày.

## Xác nhận mới từ bảng chuẩn Hạ 29/10/2026

- Thứ Năm: An Giang chính; 2ĐP = Tây Ninh + Bình Thuận theo quy ước người dùng.
- Đá thường: số cặp trúng trong một đài = min(số lần về mỗi con). Bắc52–49 đá2, mỗi con về2 lần =>2 cặp, mức trúng4; không chặn tối đa một cặp và không lấy tích số lần về.
- Trung ảnh16:58:38 dòng57–75 là đá thường1 tại một đài Quảng Bình; không phải ĐX hai đài.

## Quy trình ba bước bắt buộc

Người dùng xác nhận ngày 29/10/2026: **phân tích ảnh → ghi một file; phân tích tin nhắn TXT → ghi một file khác; sau đó tính tổng từ cả hai file**. Thực hiện tuần tự cho từng nhóm/ngày:

1. **Phân tích ảnh:** đọc hết ảnh hiện có, ghi từng nguồn và từng khoản vào `AnhCacNhom/PHAN_TICH_ANH_<nhom>_<ngay>.json`. Lưu số/cặp, mức gốc, loại, miền/đài, phạm vi mức chung, dòng gạch bỏ, giả định và nguồn chưa đọc được. Ảnh tổng/biên nhận cũng ghi rõ lý do không cộng. Lưu file xong mới sang bước 2.
2. **Phân tích TXT:** đọc toàn bộ TXT hiện có và ghi riêng vào `AnhCacNhom/PHAN_TICH_TXT_<nhom>_<ngay>.json`. Giữ giờ gửi, nội dung gốc, từng khoản đã tách, tin tham chiếu ảnh, tin xuất trùng và tin chưa đọc được. Nếu trùng khoản trong ảnh, ghi mã nguồn ảnh liên quan cùng bằng chứng, không tự bỏ chỉ vì trùng số.
3. **Tính tổng hai file:** đọc lại cả hai file đã lưu trên đĩa rồi mới cộng các khoản hợp lệ, đối chiếu trùng nguồn, tách ngày/miền/đài, dò trúng và xuất Excel theo mẫu. Bảng tổng phải truy ngược được về mã khoản trong đúng file phân tích ảnh hoặc TXT. Không tính trực tiếp từ bản đọc chưa lưu, tổng cũ hoặc số liệu mã hóa sẵn trong script. Có sửa cách đọc thì sửa file phân tích liên quan và tính lại từ cả hai file.

Hai file dùng JSON UTF-8, số đánh lưu dưới dạng chuỗi để giữ số 0 đầu. Không có nguồn của một loại vẫn tạo file phân tích ghi rõ trạng thái; thiếu nội dung không được coi là tổng bằng 0. Các giả định trong hai file phải được đưa sang đúng ô đầu vào và kết quả tô vàng trong Excel. Chi tiết trường cần lưu nằm trong hướng dẫn chính.

## Theo dõi thư mục đang cập nhật

**Trạng thái mới nhất 29/10/2026: người dùng đã yêu cầu dừng, lịch theo dõi đã bị xóa. Không tự bật lại. Chỉ thực hiện nhóm được người dùng yêu cầu trực tiếp, như Vĩnh An.** Phần dưới ghi lại quy ước của lịch cũ.

Người dùng yêu cầu cứ có file/nhóm được cập nhật trong `AnhCacNhom` thì tính và dò cho từng người, xuất Excel. **Bỏ qua Riêng Lực** vì đã tính rồi, cho tới khi người dùng đổi yêu cầu. Heartbeat của chat đang kiểm tra mỗi 5 phút. Lưu kiểm kê tên file, SHA-256/nội dung TXT vào `AnhCacNhom/NHAT_KY_THEO_DOI.json`; không có thay đổi thì im lặng. Có thay đổi thì tính lại nhóm/ngày liên quan từ từng nguồn, không cộng nối tổng cũ. Chỉ báo khi có kết quả mới, thay đổi tổng/trúng hoặc lỗi cần xử lý. Người dùng đang thêm file dần nên kiểm kê lại trước khi chốt đợt; không giữ nguyên danh sách nhóm từ đầu lượt làm việc.
