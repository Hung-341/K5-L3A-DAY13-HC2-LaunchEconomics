"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)

CHI_PHI_CO_DINH = 40_000_000   # đồng / tháng (A4)
KHOI_LUONG_THANG = 45_000      # yêu cầu / tháng ở quy mô đầy đủ (A4)
PHAM_VI_PILOT = ['noi_dia', 'hang_nang']


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        # Bỏ phần chạy vượt giới hạn; yêu cầu cần nhiều lượt hơn chuyển cho nhân viên.
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong if thanh_cong else float('nan'),
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


# ---------- Nhiệm vụ A3 · Tách theo loại ----------
def bang_theo_loai(runs, reqs):
    dong = []
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, r)
        dong.append(dict(
            loai=loai,
            so_yc=len(r),
            ti_le_tc=kq['thanh_cong'] / len(r),
            lan_chay_moi_yc=runs['request_id'].isin(r['request_id']).sum() / len(r),
            cps=kq['cps'],
            so_voi_baseline=kq['cps'] / BASELINE,
        ))
    return pd.DataFrame(dong)


def ti_le_ok_theo_attempt(runs, reqs):
    """Tỉ lệ lần chạy status=ok theo loai × attempt: bằng chứng chạy lại có giúp không."""
    m = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    m['ok'] = (m['status'] == 'ok').astype(float)
    return m.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean')


# ---------- Nhiệm vụ A4 · Chi phí cố định ----------
def chi_phi_co_dinh(runs, reqs, khoi_luong):
    """Cộng chi phí cố định/tháng vào chi phí mỗi việc thành công của phạm vi pilot.
    Giả định: tỉ lệ việc thành công của phạm vi trên toàn bộ yêu cầu (tc / 1.200) giữ nguyên ở quy mô tháng."""
    pham_vi = reqs[reqs['loai'].isin(PHAM_VI_PILOT)]
    kq = mo_hinh(runs, pham_vi)
    tc_thang = khoi_luong * kq['thanh_cong'] / len(reqs)
    co_dinh_moi_viec = CHI_PHI_CO_DINH / tc_thang
    tong_moi_viec = kq['cps'] + co_dinh_moi_viec
    return dict(khoi_luong=khoi_luong, tc_thang=tc_thang, co_dinh_moi_viec=co_dinh_moi_viec,
                cps_pham_vi=kq['cps'], tong_moi_viec=tong_moi_viec, so_voi_baseline=tong_moi_viec / BASELINE)


# ---------- Nhiệm vụ B · Độ nhạy ----------
KICH_BAN_B1 = {
    'Giá token gấp đôi':          dict(gia_vao=52, gia_ra=260),
    'Giá token giảm một nửa':     dict(gia_vao=13, gia_ra=65),
    'Tỉ lệ xem lại gấp đôi':      dict(he_so_xem_lai=2),
    'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
    'Số ca làm lại gấp đôi':      dict(he_so_lam_lai=2),
    'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
    'Lương nhân viên tăng 25%':   dict(luong_phut=2500),
    'Chỉ cho chạy tối đa 2 lần':  dict(max_lan_chay=2),
    'Chỉ cho chạy 1 lần':         dict(max_lan_chay=1),
}


def bang_do_nhay(runs, reqs):
    goc = mo_hinh(runs, reqs)['cps']
    dong = []
    for ten, kw in KICH_BAN_B1.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        dong.append(dict(kich_ban=ten, cps=cps, thay_doi_pct=(cps / goc - 1) * 100))
    return goc, pd.DataFrame(dong)


def gioi_han_chay_lai(runs, reqs):
    """B3: chi phí cả hệ thống = tổng trợ lý + 12.000 đ × số yêu cầu không thành công (nhân viên làm thay)."""
    dong = []
    for k in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - kq['thanh_cong']
        dong.append(dict(gioi_han=k, tong_tro_ly=kq['tong'], khong_thanh_cong=khong_tc,
                         ca_he_thong=kq['tong'] + khong_tc * BASELINE, cps=kq['cps']))
    return pd.DataFrame(dong)


def xem_lai_100(runs, reqs, phut_xem=5, phut_lam_lai=9):
    """B4: phạm vi noi_dia + hang_nang, xem lại 100% mọi yêu cầu có ít nhất một lần chạy ok;
    ca lam_lai (sai bị bắt trước khi gửi) tốn phut_lam_lai phút. Số giả định → simulated."""
    pham_vi = reqs[reqs['loai'].isin(PHAM_VI_PILOT)]
    r = runs[runs['request_id'].isin(pham_vi['request_id'])]
    so_ok = r.loc[r['status'] == 'ok', 'request_id'].nunique()
    so_lam_lai = int((pham_vi['ket_qua'] == 'lam_lai').sum())
    token_tool = (r['tokens_in'] / 1000 * GIA_VAO + r['tokens_out'] / 1000 * GIA_RA
                  + r['tool_calls'] * GIA_TOOL).sum()
    tien_xem = so_ok * phut_xem * LUONG_PHUT
    tien_lam_lai = so_lam_lai * phut_lam_lai * LUONG_PHUT
    tong = token_tool + tien_xem + tien_lam_lai
    tc = int((pham_vi['ket_qua'] == 'thanh_cong').sum())
    # Mức hoà vốn: số phút xem lại mỗi yêu cầu để cps = 12.000 đ
    hoa_von = (BASELINE * tc - token_tool - tien_lam_lai) / (so_ok * LUONG_PHUT)
    return dict(so_yc=len(pham_vi), so_ok=so_ok, so_lam_lai=so_lam_lai, token_tool=token_tool,
                tien_xem=tien_xem, tien_lam_lai=tien_lam_lai, tong=tong, thanh_cong=tc,
                cps=tong / tc, so_voi_baseline=tong / tc / BASELINE, phut_xem_hoa_von=hoa_von)


def vnd(x):
    """Định dạng số kiểu Việt Nam: dấu chấm ngăn nghìn."""
    return f'{x:,.0f}'.replace(',', '.')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)

    # ----- A1 -----
    kiem_tra_dap_an_biet_truoc()
    print(f'  p=0,8 tối đa 2 lần: {so_lan_chay_ky_vong(0.8, 2):.2f} · đến khi đúng: {so_lan_chay_ky_vong(0.8):.2f}'
          f' · hệ số chi phí tối đa 3 lần: {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')

    # ----- A2 -----
    print('\n== A2 · Mô hình chi phí (xem_lai, lam_lai, tong, cps là simulated) ==')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:16s} {gia_tri:>14,.1f}')
    tong = ket_qua['tong']
    print(f'cps / hoá đơn mỗi yêu cầu: {ket_qua["cps"] / ket_qua["hoa_don_moi_yc"]:.1f} lần')
    for k in ['token', 'tool', 'xem_lai', 'lam_lai']:
        print(f'  tỉ trọng {k:8s}: {ket_qua[k] / tong * 100:5.1f}%')
    print(f'  giờ nhân viên (xem lại + làm lại): {(ket_qua["xem_lai"] + ket_qua["lam_lai"]) / tong * 100:.1f}%')
    khong_tc = len(reqs) - ket_qua['thanh_cong']
    ca_he_thong = (tong + khong_tc * BASELINE) / len(reqs)
    print(f'Chi phí cả hệ thống mỗi yêu cầu = ({vnd(tong)} + {khong_tc} × 12.000) / {len(reqs)}'
          f' = {vnd(ca_he_thong)} đ = {ca_he_thong / BASELINE:.2f}× [simulated]')
    print(f'  số ca chuyen_nhan_vien: {(reqs["ket_qua"] == "chuyen_nhan_vien").sum()},'
          f' lam_lai: {(reqs["ket_qua"] == "lam_lai").sum()}')

    # ----- A3 -----
    print('\n== A3 · Theo loại (cps là simulated) ==')
    a3 = bang_theo_loai(runs, reqs)
    for _, d in a3.iterrows():
        print(f'{d.loai:10s} {d.so_yc:5d}  tc {d.ti_le_tc * 100:5.1f}%  lần chạy/yc {d.lan_chay_moi_yc:.2f}'
              f'  cps {vnd(d.cps):>7s} đ  {d.so_voi_baseline:.2f}×')
    print('Tỉ lệ ok theo attempt:')
    print((ti_le_ok_theo_attempt(runs, reqs) * 100).round(1).to_string())

    # ----- A4 -----
    print('\n== A4 · Chi phí cố định 40 triệu/tháng, phạm vi noi_dia + hang_nang [simulated] ==')
    for kl in [KHOI_LUONG_THANG, KHOI_LUONG_THANG // 2]:
        a4 = chi_phi_co_dinh(runs, reqs, kl)
        print(f'{vnd(kl):>7s} yc/tháng: {vnd(a4["tc_thang"])} việc tc · cố định {vnd(a4["co_dinh_moi_viec"])} đ/việc'
              f' · cps phạm vi {vnd(a4["cps_pham_vi"])} + cố định = {vnd(a4["tong_moi_viec"])} đ'
              f' = {a4["so_voi_baseline"]:.2f}×')

    # ----- B1 -----
    print('\n== B1 · Độ nhạy (simulated) ==')
    goc, b1 = bang_do_nhay(runs, reqs)
    print(f'{"Gốc (A2)":28s} {vnd(goc):>7s} đ')
    for _, d in b1.iterrows():
        print(f'{d.kich_ban:28s} {vnd(d.cps):>7s} đ  {d.thay_doi_pct:+6.1f}%')

    # ----- B2 -----
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'\n== B2 · Token ×2 cùng xem lại ×2: {vnd(cps_cap)} đ ({(cps_cap / goc - 1) * 100:+.1f}%) [simulated]')
    # Gom kịch bản theo yếu tố, lấy |thay đổi| lớn nhất của mỗi yếu tố rồi xếp hạng
    ten_yeu_to = ['giá token', 'giá token', 'tỉ lệ xem lại', 'tỉ lệ xem lại', 'số ca làm lại', 'số ca làm lại',
                  'lương nhân viên', 'giới hạn lượt chạy', 'giới hạn lượt chạy']
    b1['yeu_to'] = ten_yeu_to
    b1['abs'] = b1['thay_doi_pct'].abs()
    xep_hang = b1.groupby('yeu_to')['abs'].max().sort_values(ascending=False)
    print('Xếp hạng yếu tố theo |thay đổi| lớn nhất:')
    for i, (ten, gt) in enumerate(xep_hang.items(), 1):
        print(f'  {i}. {ten} ({gt:.1f}%)')
    print('Kiểm tra đối xứng (½ mức tăng khi gấp đôi = mức giảm khi giảm nửa):')
    for a, b in [(0, 1), (2, 3), (4, 5)]:
        print(f'  {b1.kich_ban[a]}: {b1.thay_doi_pct[a]:+.2f}% / 2 = {b1.thay_doi_pct[a] / 2:+.2f}%'
              f' vs {b1.thay_doi_pct[b]:+.2f}%')

    # ----- B3 -----
    print('\n== B3 · Giới hạn chạy lại (simulated) ==')
    for _, d in gioi_han_chay_lai(runs, reqs).iterrows():
        print(f'{int(d.gioi_han)} lần: trợ lý {vnd(d.tong_tro_ly)} đ · không tc {int(d.khong_thanh_cong)}'
              f' · cả hệ thống {vnd(d.ca_he_thong)} đ · cps {vnd(d.cps)} đ')

    # ----- B4 -----
    print('\n== B4 · Xem lại 100% (noi_dia + hang_nang) [simulated] ==')
    pv = reqs[reqs['loai'].isin(PHAM_VI_PILOT)]
    tb_lam_lai = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated']
    for phut_ll in [9, round(tb_lam_lai.mean(), 1)]:
        b4 = xem_lai_100(runs, reqs, phut_lam_lai=phut_ll)
        print(f'làm lại {phut_ll} phút: {b4["so_ok"]} yc ok × 5 phút = {vnd(b4["tien_xem"])} đ · '
              f'{b4["so_lam_lai"]} ca × {phut_ll} phút = {vnd(b4["tien_lam_lai"])} đ · token+tool {vnd(b4["token_tool"])} đ'
              f' → {vnd(b4["tong"])} / {b4["thanh_cong"]} = {vnd(b4["cps"])} đ = {b4["so_voi_baseline"]:.2f}×'
              f' · hoà vốn khi xem lại ≤ {b4["phut_xem_hoa_von"]:.1f} phút')
    print(f'  phút làm lại thực tế/ca lam_lai: tb {tb_lam_lai.mean():.1f}, trung vị {tb_lam_lai.median():.1f}')

    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
