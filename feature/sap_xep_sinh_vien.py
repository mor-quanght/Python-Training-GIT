from sinh_vien import Sinhvien

sort_dict = {}


def sap_xep_sinh_vien(danh_sach_sv, key_sx, loai_sx):
    for sinhvien in danh_sach_sv:
        sort_dict[sinhvien] = getattr(sinhvien, key_sx)
    danh_sach_sv = sorted(sort_dict.items(), key=lambda x: x[1], reverse=loai_sx)
    output=[]
    for data in danh_sach_sv:
        output.append(data[0])

    return output


'''
danh_sach_sv = []

sv1 = Sinhvien(1, 'b', 'nam', 20, 10, 10, 9)
sv2 = Sinhvien(2, 'c', 'nam', 21, 9, 8, 9)
sv3 = Sinhvien(3, 'ac', 'nam', 22, 9, 6, 9)

danh_sach_sv.append(sv1)
danh_sach_sv.append(sv2)
danh_sach_sv.append(sv3)

sv1.thuoc_tinh()

danh_sach_sv=(sap_xep_sinh_vien(danh_sach_sv, 'diem_tb', False))
for data in danh_sach_sv:
    print(data)
print('//////////////////////////////////////////////////////')

for data in danh_sach_sv:
    print(data)
print('//////////////////////////////////////////////////////')

print(sap_xep_sinh_vien(danh_sach_sv, 'id', True))
'''