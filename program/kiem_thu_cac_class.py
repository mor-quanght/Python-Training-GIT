from phuong_tien_giao_thong import PhuongTienGiaoThong
from oto import Oto
from hien_thi_thong_tin import hien_thi

#phuong tien giao thong

object1=PhuongTienGiaoThong("hang1", "ten2", 2000, 400.0)
list=object1.lay_thong_tin()
print(list)

object1.nhap_thong_tin("hang2", "ten2", 2000, 400.0)
list=object1.lay_thong_tin()
print(list)


print('////////////////////')

#Oto

xe_oto = Oto("hang1", "ten2", 2000, 400.0, 4, 4, 'dongco1')
print(xe_oto)
list=xe_oto.lay_thong_tin()
print(list)

print(xe_oto.van_toc_cs())
xe_oto.huy_bo()

list=xe_oto.lay_thong_tin()
print(list)


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

nhap_nhanh()