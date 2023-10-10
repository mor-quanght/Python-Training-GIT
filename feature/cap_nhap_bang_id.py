from sinh_vien import Sinhvien


def cap_nhap_bang_id(danh_sach_sv):
    id = int(input('id cua sinh vien:'))
    for sinhvien in danh_sach_sv:
        if sinhvien.id == id:
            print('Nhap thong tin sinh vien:')
            # id,ten,gioi_tinh,tuoi,diem_toan,diem_ly,diem_hoa
            id = input('id:')
            ten = input('ten:')
            gioi_tinh = input('gioi_tinh:')
            tuoi = input('tuoi:')
            diem_toan = float(input('diem_toan:'))
            diem_ly = float(input('diem_ly:'))
            diem_hoa = float(input('diem_hoa:'))
            sinhvien.cap_nhap(id, ten, gioi_tinh, tuoi,
                              diem_toan, diem_ly, diem_hoa)
            print('Da duoc cap nhap')
            return None

    print('Khong tim thay sinh vien nay')
