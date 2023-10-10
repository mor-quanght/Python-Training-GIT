def hoc_luc(diem_tb):
    if diem_tb < 5:
        return 'Yeu'
    elif diem_tb < 6.5:
        return 'Trung Binh'
    elif diem_tb < 8:
        return 'Kha'
    else:
        return 'Gioi'


class Sinhvien:
    def __init__(self, id, ten, gioi_tinh, tuoi, diem_toan, diem_ly, diem_hoa):
        self.id = id
        self.ten = ten
        self.gioitinh = gioi_tinh
        self.tuoi = tuoi
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa
        self.diem_tb = int((diem_toan + diem_ly + diem_hoa) / 3)
        self.hocluc = hoc_luc(self.diem_tb)

    def __str__(self):
        return f'{self.id},{self.ten},{self.gioitinh},{self.tuoi},' \
               f'{self.diem_toan},{self.diem_ly},{self.diem_hoa},' \
               f'{self.diem_tb},{self.hocluc}'

    def cap_nhap(self, id, ten, gioi_tinh, tuoi, diem_toan, diem_ly, diem_hoa):
        self.id = id
        self.ten = ten
        self.gioitinh = gioi_tinh
        self.tuoi = tuoi
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa
        self.diem_tb = int((diem_toan + diem_ly + diem_hoa) / 3)
        self.hocluc = hoc_luc(self.diem_tb)

    def xoa(self):
        del self

    def thuoc_tinh(self):
        print(f'id,ten,gioi tinh, tuoi, diem toan, diem ly,'
              f' diem hoa, diem tb, hoc luc')