# Team

## Thông tin nhóm

- Tên nhóm: HC2
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-HC2-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/Hung-341/K5-L3A-DAY13-HC2-LaunchEconomics · `main` · commit chốt:

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Đặng Đức Cương | 2A202603680 |  |  | Người viết code, kiêm người kiểm số (A–B); người gắn nhãn 1 (C) |
|   2 | Lê Gia Hưng | 2A202603706 |  | Hung-341 | Người gắn nhãn 2, kiêm giữ hồ sơ (C, D, E1–E3) |
|   3 |        |      |       |        |         |
|   4 |        |      |       |        |         |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## LeGiaHung-2A202603706

### Phần việc phụ trách

- Nhiệm vụ C/E1: hoàn thiện E1 trong `report/team/chi_so.md`; tổng hợp hai bộ nhãn, tỉ lệ đồng thuận và bảng khắc phục trong `report/team/bang_loi.md`.
- Nhiệm vụ D: tính cỡ mẫu, chọn cách chia pilot và hoàn thiện `report/team/pilot_plan.yaml`.
- Nhiệm vụ E2–E3: điền risk register và các phần hồ sơ được giao trong `report/team/chi_so.md` và `report/team/ho_so_launch_v0.md`.
- Người gắn nhãn 2 ở CP3: gắn nhãn 20 ca độc lập trước khi so với bộ nhãn còn lại.

### Đóng góp cụ thể

- Viết phần CP4 trong `src/lab13.py` tính năm trường hợp cỡ mẫu D1, power 0,64 và tỉ lệ mở lại; ghi đánh đổi khi chọn MDE 6 điểm và trả lời năm câu D2.
- Tính E1 trên 1.200 yêu cầu: chỉ số chính 82,83% (994/1.200), tỉ lệ sửa/bỏ gợi ý 27,12% (48/177), tỉ lệ mở lại 4,25% (51/1.200); lập danh sách event và kiểm tra chéo event với chỉ số.
- Gắn bộ nhãn 2 cho 20 ca; so với bộ nhãn 1, đạt đồng thuận 18/20 = 90%; viết quy tắc cho ca 13, 18 và bảng khắc phục năm loại.
- Đề xuất ba luật dừng cho an toàn, chi phí và mức sử dụng; ghi rollback và ngày quyết định.
- Điền hai rủi ro kinh tế theo bảng độ nhạy B1; tích hợp số A–C, pilot và rủi ro vào hồ sơ launch.

### Bằng chứng

- Phần CP4 trong `src/lab13.py`; `report/team/pilot_plan.yaml`: D1/D2 và ba stop rule; `report/team/bang_loi.md`; E1 và E2 trong `report/team/chi_so.md`; bảy mục và đề xuất trong `report/team/ho_so_launch_v0.md`.

## DangDucCuong-2A202603680

### Phần việc phụ trách

- Code và kinh tế: nhiệm vụ A (CP1) và B (CP2) trong `src/lab13.py`; phần A–B của `report/team/bang_chi_phi.md`.
- Người gắn nhãn 1 ở CP3: gắn nhãn 20 ca độc lập trước khi so với bộ nhãn 2.

### Đóng góp cụ thể

- Viết ba hàm A1 (ba phép thử ĐẠT 1,20 · 1,25 · 1,25) và `mo_hinh(...)` có tham số giá, lương, hệ số xem lại/làm lại, `max_lan_chay`.
- Tính A2, A3 (theo `loai` + tỉ lệ ok theo `attempt`), A4 (cố định 40 triệu/tháng, phạm vi `noi_dia + hang_nang`), B1 (9 kịch bản), B2, B3, B4.
- Bàn giao cho người giữ hồ sơ: cps 4.472 đ [simulated]; phạm vi pilot `noi_dia + hang_nang` 3.414 đ, + cố định = 4.599 đ (0,38×) [simulated]; ba yếu tố nhạy nhất: số ca làm lại, tỉ lệ xem lại, lương; giới hạn 2 lượt chạy rẻ nhất cho cả hệ thống; xem lại 100% = 0,98×–1,03× [simulated].
- Giả định: chi phí cả hệ thống cộng 12.000 đ cho mỗi yêu cầu không thành công; A4 giữ tỉ lệ 900/1.200 việc thành công ở quy mô 45.000 yêu cầu/tháng; B4 dùng 5 phút xem lại, 9 phút làm lại (thêm kịch bản 15,3 phút).

### Bằng chứng

- `src/lab13.py`, `report/team/bang_chi_phi.md`, báo cáo cá nhân `report/team/2A202603680_DangDucCuong.md`.
- Số đối chiếu khớp hướng dẫn chi tiết (lệch dưới 2%): 978 việc thành công, tổng 4.373.585 đ, 4.472 đ/việc thành công [simulated].
