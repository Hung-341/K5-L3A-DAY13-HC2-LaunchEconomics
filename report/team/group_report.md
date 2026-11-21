# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: HC2
- Lớp: L3A
- Thành viên: Nguyễn Trần Anh Khôi (2A202603422), Lê Gia Hưng (2A202603706), Đặng Đức Cương (2A202603680). Xem `TEAM.md`.

## 2. Mục tiêu và cách tiếp cận

Nhóm đánh giá chi phí trên mỗi yêu cầu hoàn phí thành công, mức sử dụng, loại lỗi và thiết kế pilot có nhóm đối chứng. Dữ liệu của lab là giả lập. Nhóm chia việc A–B cho Khôi, C/E1 cho Cương, D/E2–E3 cho Hưng; hai bộ nhãn CP3 phải được lập độc lập trước khi so.

## 3. Giải pháp

- A–B: Khôi phụ trách `src/lab13.py` và `report/team/bang_chi_phi.md` theo dữ liệu trace.
- C/E1: Cương phụ trách hai bộ nhãn, bảng khắc phục trong `bang_loi.md`, chỉ số và event trong `chi_so.md`.
- D/E2–E3: Hưng phụ trách `pilot_plan.yaml`, risk register và các mục hồ sơ launch được giao.

## 4. Kết quả

Thiết kế pilot chọn 20 nhân viên mỗi nhánh, MDE 6 điểm và 859 yêu cầu hiệu dụng mỗi nhánh (DE 6,96). Nếu tác động thật là 5 điểm, power khoảng 0,64. Tỉ lệ mở lại hiện tại là 4,25% toàn mẫu và 3,97% trong scope `noi_dia + hang_nang` [simulated]. Đề xuất trong hồ sơ là Go có điều kiện, với các điều kiện và người phụ trách ghi tại `ho_so_launch_v0.md`.

## 5. Khó khăn và cách xử lý

Với 40 nhân viên, cách chia theo cụm không đủ cỡ mẫu để phát hiện mức chênh 5 điểm. Nhóm chọn MDE 6 điểm và ghi rõ power giảm còn khoảng 0,64 nếu tác động thực là 5 điểm. Các con số kinh tế phải gắn nhãn simulated.

## 6. Tổng hợp đóng góp

Khôi phụ trách A–B; Cương phụ trách C/E1; Hưng phụ trách D/E2–E3, giữ fork và tích hợp. Chi tiết theo file và bằng chứng được ghi trong `TEAM.md` và báo cáo cá nhân.

## 7. Hạn chế và hướng cải thiện

Mẫu thử và thời gian xem lại/làm lại đều giả lập; chưa có nhóm đối chứng trong đợt chạy thử để kết luận tác động. Pilot cần ghi event có `trace_id`, đo phút làm việc thật và theo dõi an toàn trước khi mở rộng.

## 8. Tài liệu tham khảo

- `README.md`, `RULES.md`, `CHECKPOINTS.md`, `RUBRIC.md`, `SUBMISSION.md`.
- `docs/du_lieu_va_cong_thuc.md` và `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
