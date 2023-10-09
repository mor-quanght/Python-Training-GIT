from nhap_ptgt import nhap_ptgt
from nhap_n_oto import nhap_n_oto
from hien_thi_thong_tin import hien_thi
from oto import Oto


def nhap_hienthi_ptgt():
    # Nhap phuong tien giao thong
    ptgt = nhap_ptgt()

    # Hien thi thong tin
    print(ptgt.descriptors())
    print(ptgt)

# Nhap thong tin Oto
def nhap_hien_thi_oto():
    danh_sach_oto = nhap_n_oto()

    # Hien thi thong tin Oto
    print(danh_sach_oto[0].descriptors())
    hien_thi(danh_sach_oto)



def nhap_nhanh():
    danh_sach_oto = []

    xe_oto = Oto("hang1", "ten2", 2000, 400.0, 4, 4, 'dongco1')
    danh_sach_oto.append(xe_oto)

    xe_oto = Oto("hang3", "ten3", 1765, 500.0, 4, 4, 'dongco2')
    danh_sach_oto.append(xe_oto)

    xe_oto = Oto("hang3", "ten4", 1964, 200.0, 4, 4, 'dongco3')
    danh_sach_oto.append(xe_oto)

    print(danh_sach_oto[0].descriptors())
    hien_thi(danh_sach_oto)

nhap_hienthi_ptgt()
#nhap_hien_thi_oto()

