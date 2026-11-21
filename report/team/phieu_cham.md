# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

> **Trạng thái: HC2 đã chốt điểm (Đặng Đức Cương, Lê Gia Hưng).
- Nhóm chấm (hội đồng): HC2
- Nhóm được chấm: Alone

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 8 | Go có điều kiện khớp 0,38× [simulated]; tự ghi **Bất lợi**: xem lại 100% = 0,98× (1,03× nếu làm lại 15,3 phút) và power 0,64 nếu tác động thật là 5 điểm; mỗi điều kiện có vai trò và ngày kiểm tra. Trừ 2: cách xử lý khi sửa + bỏ vẫn 21,1% (≥ 15%) chỉ ghi "áp dụng luật dừng chi phí", chưa nói đề xuất và ngày quyết định 2027-01-12 thay đổi thế nào nếu phạm vi bị thu hẹp về noi_dia |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 9 | Nhãn [simulated] ở mục 1, 2, 3, 7, ở A2–B4 và danh sách `simulated_inputs` (6 dòng). Phạm vi chỉ noi_dia (0,22×) + hang_nang (0,69×), loại quoc_te (1,88×, thành công 27,3%) và doi_tac (0,85×) [simulated]. Trừ 1: một số ngưỡng suy ra từ số simulated chưa có nhãn tại chỗ dùng, ví dụ "giữ xem lại ≤ 64%" trong đề xuất hồ sơ và ngưỡng 8.000 đ trong luật dừng chi phí |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 9 | Đối chứng 20 + 20 nhân viên cùng thời gian, seed 13, phân tầng theo depot; bước 50% chạy 14 ngày (≈ 430 ≥ 299 yêu cầu/người), theo dõi đến 2027-01-10, quyết định 2027-01-12. Bốn luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ, có ngưỡng, thời hạn và vai trò; luật mở lại theo cohort đủ 7 ngày, ≥ 800 yêu cầu. Trừ 1: luật chi phí có thể kích hoạt cuối tuần 3 (2026-12-27, giữa bước 50%) mà kế hoạch chưa ghi trước chỉ số chính sẽ đo trên phạm vi nào và lịch thay đổi ra sao |
| **Tổng** | | | | **26 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Số A–B khớp đáp án, mọi con số bất lợi đều được nêu kèm người xử lý và ngày kiểm tra, kế hoạch đủ cụm, đủ thời gian theo dõi. Điều kiện còn lại: chính sách xem lại và luật chi phí có thể va nhau. Đợt chạy thử có sửa + bỏ 21,1% (≥ ngưỡng 15%), nên nếu không giảm được thì xem lại giữ 100% = 11.743 đ/việc [simulated] > 8.000 đ, và luật chi phí (tính từ tuần 2, 2 tuần liên tiếp) sẽ kích hoạt cuối tuần 3 (2026-12-27), giữa bước 50%. Alone cần ghi trước chỉ số chính sẽ đo trên phạm vi nào nếu bị thu hẹp về noi_dia. Ngoài phạm vi chấm của hội đồng: mục 5 ghi hai bộ nhãn lỗi đều do AI gắn; nhóm nên ghi rõ bằng chứng coach cho phép.

**Một câu hỏi cho đội trình:** Nếu sửa + bỏ vẫn ở mức 21,1% nên xem lại giữ 100% (11.743 đ > 8.000 đ [simulated]), luật chi phí sẽ thu hẹp về noi_dia trước bước 50%; khi đó chỉ số chính đo trên phạm vi nào, và 20 + 20 nhân viên có còn đủ 299 yêu cầu noi_dia mỗi người trong 14 ngày không?

**Câu trả lời của đội trình (ghi lại tại buổi):** Luật chi phí kích hoạt cuối tuần 3 (2026-12-27), tức sau khi bước 50% đã bắt đầu; từ 2026-12-28 chỉ số chính chỉ đo trên noi_dia vì can thiệp đã đổi, nên 7 ngày còn lại chỉ được khoảng 180 yêu cầu/người (< 299), phải chạy 12 ngày đến 2027-01-08 (≈ 309 yêu cầu/người, n hiệu dụng 863) và lùi ngày quyết định sang sau 2027-01-15. Thu hẹp chưa giải quyết được chi phí: noi_dia xem lại 100% vẫn tốn 11.301 đ = 0,94× [simulated] và sửa + bỏ 18,3% chưa đạt ngưỡng 15%, nên nếu không giảm được xem lại xuống ≤ 68% thì Alone sẽ đề xuất No-go cho việc mở rộng; nhánh này kế hoạch hiện tại chưa ghi và nhóm sẽ bổ sung.

**Ghi chú kiểm tra của hội đồng:** HC2 tính lại bằng `src/lab13.py` và dữ liệu lab: noi_dia ≈ 25,75 yêu cầu/người/ngày → 7 ngày ≈ 180, 12 ngày = 309, n hiệu dụng = 20 × 309 ÷ (1 + 308 × 0,02) ≈ 863; noi_dia xem lại 100% = (token + tool + 813 × 5 × 2.000 + 30 × 9 × 2.000) ÷ 783 = 11.301 đ [simulated]; mức xem lại tối đa để ≤ 8.000 đ là 68,2% [simulated]; sửa + bỏ noi_dia 17/93 = 18,3%. Mọi số khớp; mốc 2026-12-27 đúng (câu hỏi của HC2 ghi "trước bước 50%" là chưa chính xác). Câu trả lời xác nhận kế hoạch hiện tại chưa ghi nhánh này, nên điểm giữ nguyên 26/30.
