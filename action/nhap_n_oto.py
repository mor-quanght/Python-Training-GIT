from oto import Oto


def nhap_n_oto():
    danh_sach_oto = []

    n = int(input('So xe Oto muon nhap: '))
    for count in range(n):
        print('Nhap thong tin Oto')
        # hang_sx, ten_phuong_tien, nam_sx, van_toc_toi_da,so_cho_ngoi, so_banh, dong_co

        hang_sx = input('Nhap hang san xuat(string): ')
        ten_phuong_tien = input('Nhap ten_phuong_tien(string): ')
        nam_sx = int(input('Nhap nam_sx(int): '))
        van_toc_toi_da = float(input('Nhap van_toc_toi_da(float): '))
        so_cho_ngoi = int(input('Nhap so_cho_ngoi(int): '))
        so_banh = int(input('Nhap so_banh(int): '))
        dong_co = input('Nhap dong_co(string): ')

        danh_sach_oto.append(Oto(hang_sx, ten_phuong_tien, nam_sx,
                                 van_toc_toi_da, so_cho_ngoi, so_banh,
                                 dong_co))

    return danh_sach_oto


