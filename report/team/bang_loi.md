# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Đặng Đức Cương · Người gắn nhãn 2: Lê Gia Hưng (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Hệ thống | Không | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 18 / 20 = 90%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Ca 13 (thống nhất: Giới hạn hệ thống): yêu cầu nằm ngoài phạm vi trợ lý thì gốc lỗi là giới hạn, kể cả khi trợ lý trả lời chung chung thay vì nói rõ mình không xử lý được; cách trả lời kém được xử lý ở cột khắc phục.
- Ca 18 (thống nhất: Ngữ cảnh): số tiền tính đúng chính sách thì không phải lỗi hệ thống; lỗi nằm ở giả định khách tự hiểu cách tính 30.000 đ × 50%.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `refund_ledger_write` có `ket_qua` = lỗi tài khoản từ ngân hàng; cảnh báo khi vượt 1% số lệnh hoàn trong ngày | Kiểm tra độ dài và định dạng số tài khoản trước khi tạo lệnh; yêu cầu khách xác nhận lại số tài khoản | PM trợ lý hoàn phí |
| 20 | Hệ thống | Đối soát mỗi giờ: hơn một bản ghi `refund_ledger_write` thành công cho cùng `request_id`; ngưỡng 0 ca | Gắn `idempotency_key` theo `request_id` cho mọi lệnh hoàn; lệnh trùng bị chặn và trả về trạng thái của lệnh đầu | Kỹ sư trưởng agent |
| 16 | Ngữ cảnh | Tỉ lệ phản ánh bị làm phiền trên thông báo gửi từ 22:00 đến 7:00, theo tuần; ngưỡng 0,5% số thông báo | Thông báo không khẩn được hẹn gửi sau 7:00; lệnh hoàn vẫn ghi sổ cái ngay | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason` = đơn quá 12 tháng, đếm theo tuần; xem xét mở rộng dữ liệu khi vượt 2% số yêu cầu | Kiểm tra ngày tạo đơn ở bước đầu để báo khách sớm; giữ cách chuyển nhân viên kèm tóm tắt | PM trợ lý hoàn phí |
| 5 | Ngầm | Event `audit_sample_checked`: kiểm tra 100 đơn có mã giảm giá mỗi tuần, so số tiền đã hoàn với giá sau giảm; ngưỡng 1% đơn lệch | Tool tra giá trả về giá sau giảm; thêm phép thử cho đơn có mã giảm giá trước mỗi lần cập nhật | Kế toán trưởng |
