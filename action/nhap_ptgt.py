from phuong_tien_giao_thong import PhuongTienGiaoThong


def nhap_ptgt():
    print('Nhap thong tin phuong tien giao thong')
    # hang_sx, ten_phuong_tien, nam_sx, van_toc_toi_da

    hang_sx = input('Nhap hang san xuat(string): ')
    ten_phuong_tien = input('Nhap ten_phuong_tien(string): ')
    nam_sx = int(input('Nhap nam_sx(int): '))
    van_toc_toi_da = float(input('Nhap van_toc_toi_da(float): '))

    ptgt = PhuongTienGiaoThong(hang_sx, ten_phuong_tien, nam_sx, van_toc_toi_da)

    return ptgt
