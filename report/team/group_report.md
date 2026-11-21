# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: HC2
- Lớp: L3A
- Thành viên: Lê Gia Hưng (2A202603706), Đặng Đức Cương (2A202603680). Xem `TEAM.md`.

## 2. Mục tiêu và cách tiếp cận

Nhóm đánh giá chi phí trên mỗi yêu cầu hoàn phí thành công, mức sử dụng, loại lỗi và thiết kế pilot có nhóm đối chứng. Dữ liệu của lab là giả lập. Cương phụ trách A–B; Hưng phụ trách C/E1 và D/E2–E3. Ở CP3, mỗi người gắn một bộ nhãn độc lập rồi mới so.

## 3. Giải pháp

- A–B: Cương viết `src/lab13.py` (CP1, CP2) và điền `report/team/bang_chi_phi.md` từ dữ liệu trace.
- C: Cương gắn bộ nhãn 1, Hưng gắn bộ nhãn 2; Hưng tổng hợp tỉ lệ đồng thuận, quy tắc cho ca lệch và bảng khắc phục trong `bang_loi.md`.
- E1: Hưng tính ba chỉ số, lập danh sách event và kiểm tra chéo trong `chi_so.md`.
- D/E2–E3: Hưng viết phần D1 trong `src/lab13.py` (CP4), `pilot_plan.yaml`, risk register và tích hợp `ho_so_launch_v0.md`.

## 4. Kết quả

- Chi phí mỗi việc thành công: 4.472 đ trên toàn mẫu, gấp 16,3 lần hoá đơn token và tool chia số yêu cầu [simulated]. Trong phạm vi `noi_dia + hang_nang`, chi phí là 4.599 đ đã cộng phí cố định, bằng 0,38× của 12.000 đ [simulated].
- Ba yếu tố nhạy nhất: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%) và lương (+23,1%) [simulated].
- Bảng lỗi: hai bộ nhãn đồng thuận 18/20 = 90%; ca 13 và 18 lệch và đã được thống nhất.
- Chỉ số trong đợt chạy thử: 82,83% yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày (994/1.200); tỉ lệ sửa/bỏ gợi ý 27,12% (48/177); tỉ lệ mở lại 4,25% (51/1.200).
- Pilot: 20 nhân viên mỗi nhánh, MDE 6 điểm, 859 yêu cầu mỗi nhánh (DE 6,96). Nếu tác động thật là 5 điểm, power chỉ khoảng 0,64.
- Đề xuất: Go có điều kiện. Điều kiện và người phụ trách ghi trong `ho_so_launch_v0.md`.
- Duyệt chéo Gate 2a: nhóm Alone chấm HC2 25/30, Go có điều kiện; HC2 đã kéo bước 50% lên 2 tuần (≈ 430 yêu cầu/người ≥ 299) và ghi ngày bắt đầu chậm nhất 2026-12-01 để 2027-01-05 đủ 7 ngày theo dõi mở lại. HC2 chấm Alone 26/30 (8 · 9 · 9), Go có điều kiện; phiếu trong `phieu_cham.md`.

## 5. Khó khăn và cách xử lý

Với 40 nhân viên, chia theo cụm không đủ cỡ mẫu để phát hiện mức chênh 5 điểm. Nhóm chọn MDE 6 điểm và ghi rõ power còn khoảng 0,64 nếu tác động thật là 5 điểm. Hai bộ nhãn lệch ở ca 13 (giới hạn hay hệ thống) và ca 18 (ngữ cảnh hay hệ thống); nhóm chốt theo nguyên nhân gốc và ghi quy tắc phân biệt trong `bang_loi.md`.

## 6. Tổng hợp đóng góp

Cương phụ trách A–B và bộ nhãn 1. Hưng phụ trách C/E1, D/E2–E3, bộ nhãn 2, giữ fork và tích hợp. Chi tiết theo file và bằng chứng nằm trong `TEAM.md` và báo cáo cá nhân.

## 7. Hạn chế và hướng cải thiện

Mẫu thử và thời gian xem lại, làm lại đều giả lập; đợt chạy thử không có nhóm đối chứng nên chưa kết luận được tác động. Pilot cần ghi event có `trace_id`, đo phút làm việc thật và theo dõi an toàn trước khi mở rộng.

## 8. Tài liệu tham khảo

- `README.md`, `RULES.md`, `CHECKPOINTS.md`, `RUBRIC.md`, `SUBMISSION.md`.
- `docs/du_lieu_va_cong_thuc.md` và `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
