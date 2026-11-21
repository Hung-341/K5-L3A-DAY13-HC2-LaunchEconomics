# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: HC2 · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ trên toàn mẫu (978 việc thành công); 4.599 đ trong phạm vi noi_dia + hang_nang, đã cộng 1.185 đ cố định ở 45.000 yêu cầu/tháng [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Số ca làm lại ×2: +51,8%; tỉ lệ xem lại ×2: +40,7%; lương +25%: +23,1%; giá token ×2 chỉ +5,6% [simulated] | Giả lập | Kỹ sư trưởng agent |
| 3 · So với nhân viên tự làm | Phạm vi pilot: 4.599 đ = 0,38× của 12.000 đ (0,48× ở nửa khối lượng); quoc_te 1,88× và doi_tac 0,85× nên bị loại khỏi phạm vi [simulated] | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử: đóng trong 24 giờ và không mở lại 82,83% (994/1.200); sửa/bỏ gợi ý 27,12% (48/177); mở lại 4,25% (51/1.200) | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Hai bộ nhãn độc lập đồng thuận 18/20 = 90%; ca 13 và 18 đã thống nhất; bảng khắc phục đủ năm loại (ca 1, 20, 16, 19, 5) | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | 20 nhân viên/nhánh; MDE 6 điểm; 859 yêu cầu/nhánh; DE 6,96; power khoảng 0,64 nếu tác động thật là 5 điểm; mở lại hiện tại 4,25% | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại ×2: 6.787 đ/việc (+51,8%); review 100%: 11.743 đ/việc [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện.** Trước 2027-01-05, Kỹ sư trưởng agent sửa khoá chống trùng và đối soát sổ cái; Giám đốc vận hành chấp nhận MDE 6 điểm (power khoảng 0,64 nếu tác động thật là 5 điểm); PM bật event có `trace_id` và thay phút simulated bằng số đo thật sau tuần 1; Trưởng nhóm CSKH giảm xem lại theo bậc vì xem lại 100% tốn 11.743 đ/việc [simulated].
