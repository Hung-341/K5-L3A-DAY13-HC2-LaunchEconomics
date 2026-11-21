# Báo cáo cá nhân — DangDucCuong-2A202603680

## 1. Thông tin thành viên

- Họ tên: Đặng Đức Cương
- MSSV: 2A202603680
- Email:
- Vai trong nhóm: người viết code, kiêm người kiểm số (A–B)

## 2. Phần việc phụ trách

- Nhiệm vụ A (CP1): ba hàm A1, hàm `mo_hinh` (A2), bảng theo loại (A3), chi phí cố định (A4) trong `src/lab13.py`.
- Nhiệm vụ B (CP2): bảng độ nhạy B1, cặp yếu tố và xếp hạng B2, giới hạn chạy lại B3, xem lại 100% B4.
- Điền phần A–B của `report/team/bang_chi_phi.md` và bàn giao số cho người giữ hồ sơ.

## 3. Đóng góp cụ thể

- Viết `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`; ba phép thử in ĐẠT (1,20 · 1,25 · 1,25).
- Viết `mo_hinh(...)` có tham số giá token/tool, lương, hệ số xem lại/làm lại, `max_lan_chay`: tử số tính token + tool của **mọi** lần chạy (kể cả `status = loi`) + phút xem lại/làm lại; mẫu số chỉ đếm `ket_qua == 'thanh_cong'`. Khi giới hạn lượt chạy, bỏ lần chạy vượt giới hạn và chuyển yêu cầu đó sang `chuyen_nhan_vien`.
- Nhiệm vụ B gọi lại `mo_hinh` cho từng kịch bản, không chép công thức riêng cho từng hàng.
- Viết thêm: `bang_theo_loai`, `ti_le_ok_theo_attempt`, `chi_phi_co_dinh`, `bang_do_nhay`, `gioi_han_chay_lai`, `xem_lai_100` (có tính mức hoà vốn phút xem lại).

## 4. Bằng chứng

- File: `src/lab13.py`, `report/team/bang_chi_phi.md`.
- Con số chính (đối chiếu với hướng dẫn chi tiết, lệch 0%):
  - A2: tổng 4.373.585 đ [simulated], 978 việc thành công, **4.472 đ/việc thành công** [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ).
  - A3: noi_dia 0,22× · hang_nang 0,69× · quoc_te 1,88× · doi_tac 0,85× so với 12.000 đ [simulated].
  - A4: 4.599 đ (0,38×) ở 45.000 yêu cầu/tháng; 5.784 đ (0,48×) ở nửa khối lượng [simulated].
  - B1/B2: xếp hạng số ca làm lại (+51,8%) > tỉ lệ xem lại (+40,7%) > lương (+23,1%) [simulated]; token ×2 + xem lại ×2 = 6.543 đ (+46,3%).
  - B3: giới hạn 2 lần rẻ nhất cho cả hệ thống (6.901.220 đ) [simulated]; giới hạn 1 lần cho cps thấp nhất (4.111 đ).
  - B4: xem lại 100% = 11.743 đ = 0,98× (làm lại 9 phút), 12.415 đ = 1,03× (làm lại 15,3 phút) [simulated].
- Commit: `fe35a1b` — feat(lab13): hoan thanh nhiem vu mo hinh chi phi, do nhay va bao cao ca nhan Dang Duc Cuong

## 5. Công cụ AI đã dùng

- Claude Code: gợi ý code cho các hàm A1, `mo_hinh` và các bảng A3–B4, định dạng bảng trong `bang_chi_phi.md`.
- Cách tự kiểm tra:
  - Chạy `python lab13.py` trong `src/`: ba phép thử A1 in ĐẠT.
  - Đối chiếu từng số A2, A3, A4, B1–B4 với bảng số tự đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`: khớp, lệch dưới 2%.
  - Kiểm tra quy tắc đối xứng B1: mức giảm khi ÷2 bằng đúng nửa mức tăng khi ×2 (2,81% · 20,35% · 25,88%).
  - Tính tay: cps = 4.373.585 ÷ 978 = 4.472 đ; chi phí cả hệ thống = (4.373.585 + 222 × 12.000) ÷ 1.200 = 5.865 đ.

## 6. Tự đánh giá

- Hiểu và giải thích được: tử số tính mọi lần chạy vì lần lỗi vẫn tốn token, tool; mẫu số chỉ đếm việc thành công vì đó là giá trị thật nhận được; chi phí cả hệ thống (5.865 đ/yêu cầu) cao hơn cps (4.472 đ) vì phải cộng 222 yêu cầu nhân viên làm thay với 12.000 đ mỗi ca.
- Điểm cần cải thiện: các số xem lại, làm lại là simulated; pilot cần đo thật tỉ lệ làm lại và thời gian xem lại vì đây là hai yếu tố nhạy nhất.
