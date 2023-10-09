from phuong_tien_giao_thong import PhuongTienGiaoThong
from oto import Oto

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

