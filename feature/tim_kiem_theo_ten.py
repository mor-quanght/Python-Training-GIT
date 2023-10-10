from sinh_vien import Sinhvien


def tim_kiem_theo_ten(danh_sach_sv):
    ten = input('ten cua sinh vien:')
    for sinhvien in danh_sach_sv:
        if ten in sinhvien.ten:
            print(sinhvien)
            return None

    print('Khong tim thay sinh vien nay')

