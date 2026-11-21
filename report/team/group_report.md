# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: HC2
- Lớp: L3A
- Thành viên hiện tại: Lê Gia Hưng (2A202603706), Đặng Đức Cương (2A202603680). Xem `TEAM.md`.

## 2. Mục tiêu và cách tiếp cận

Nhóm đánh giá chi phí trên mỗi yêu cầu hoàn phí thành công, mức sử dụng, loại lỗi và thiết kế pilot có nhóm đối chứng. Dữ liệu của lab là giả lập. Cương phụ trách A–B; Hưng tiếp nhận C/E1 cùng D/E2–E3. Hai bộ nhãn CP3 phải được lập độc lập trước khi so.

## 3. Giải pháp

- A–B: Cương phụ trách `src/lab13.py` (CP1, CP2) và `report/team/bang_chi_phi.md` theo dữ liệu trace.
- C/E1: Hưng tiếp nhận phần việc này; điền E1, event và kiểm tra chéo trong `chi_so.md`, phụ trách một bộ nhãn CP3 độc lập và tích hợp bảng khắc phục. Bảng nhãn chưa hoàn tất khi chưa có đủ hai bộ được lập riêng.
- D/E2–E3: Hưng phụ trách phần D1 trong `src/lab13.py` (CP4), `pilot_plan.yaml`, risk register và tích hợp `ho_so_launch_v0.md`.

## 4. Kết quả

Chi phí mỗi việc thành công là 4.472 đ trên toàn mẫu, gấp 16,3 lần hoá đơn token và tool chia số yêu cầu [simulated]. Trong phạm vi `noi_dia + hang_nang`, chi phí là 4.599 đ đã cộng phí cố định, bằng 0,38× của 12.000 đ [simulated]. Ba yếu tố nhạy nhất là số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%) và lương (+23,1%) [simulated]. Chỉ số trong đợt chạy thử: 82,83% yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày (994/1.200); tỉ lệ sửa/bỏ gợi ý 27,12% (48/177); tỉ lệ mở lại 4,25% (51/1.200). Thiết kế pilot chọn 20 nhân viên mỗi nhánh, MDE 6 điểm và 859 yêu cầu mỗi nhánh (DE 6,96). Nếu tác động thật là 5 điểm, power khoảng 0,64. Đề xuất trong hồ sơ là Go có điều kiện, với các điều kiện và người phụ trách ghi tại `ho_so_launch_v0.md`.

## 5. Khó khăn và cách xử lý

Với 40 nhân viên, cách chia theo cụm không đủ cỡ mẫu để phát hiện mức chênh 5 điểm. Nhóm chọn MDE 6 điểm và ghi rõ power giảm còn khoảng 0,64 nếu tác động thực là 5 điểm. Các con số kinh tế phải gắn nhãn simulated.

## 6. Tổng hợp đóng góp

Cương phụ trách A–B; Hưng tiếp nhận C/E1, phụ trách D/E2–E3, giữ fork và tích hợp. Chi tiết theo file và bằng chứng được ghi trong `TEAM.md` và báo cáo cá nhân.

## 7. Hạn chế và hướng cải thiện

Mẫu thử và thời gian xem lại/làm lại đều giả lập; chưa có nhóm đối chứng trong đợt chạy thử để kết luận tác động. Pilot cần ghi event có `trace_id`, đo phút làm việc thật và theo dõi an toàn trước khi mở rộng.

## 8. Tài liệu tham khảo

- `README.md`, `RULES.md`, `CHECKPOINTS.md`, `RUBRIC.md`, `SUBMISSION.md`.
- `docs/du_lieu_va_cong_thuc.md` và `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
