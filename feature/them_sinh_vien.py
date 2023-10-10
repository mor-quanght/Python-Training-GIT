from sinh_vien import Sinhvien


def them_sinh_vien():
    print('Nhap thong tin sinh vien:')
    # id,ten,gioi_tinh,tuoi,diem_toan,diem_ly,diem_hoa
    id = int(input('id:'))
    ten = input('ten:')
    gioi_tinh = input('gioi_tinh:')
    tuoi = int(input('tuoi:'))
    diem_toan = float(input('diem_toan:'))
    diem_ly = float(input('diem_ly:'))
    diem_hoa = float(input('diem_hoa:'))

    return Sinhvien(id, ten, gioi_tinh, tuoi, diem_toan, diem_ly, diem_hoa)
