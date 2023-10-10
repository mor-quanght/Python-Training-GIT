from sinh_vien import Sinhvien


def xoa_bang_id(danh_sach_sv):
    id = int(input('id cua sinh vien:'))
    for sinhvien in danh_sach_sv:
        if sinhvien.id == id:
            danh_sach_sv.remove(sinhvien)
            print('Da xoa')
            return danh_sach_sv
    print('Khong tim thay sinh vien nay')
