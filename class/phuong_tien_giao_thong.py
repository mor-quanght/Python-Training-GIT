class PhuongTienGiaoThong:
    def __init__(self, hang_sx, ten_phuong_tien, nam_sx, van_toc_toi_da):
        if not isinstance(hang_sx, str):
            raise TypeError("hang_sx phải là string")
        if not isinstance(ten_phuong_tien, str):
            raise TypeError("ten_phuong_tien phải là string")
        if not isinstance(nam_sx, int):
            raise TypeError("nam_sx phải là int")
        if not isinstance(van_toc_toi_da, float):
            raise TypeError("van_toc_toi_da phải là float")

        self.Hang_sx = hang_sx
        self.ten_phuong_tien = ten_phuong_tien
        self.nam_sx = nam_sx
        self.van_toc_toi_da = van_toc_toi_da

    def nhap_thong_tin(self, hang_sx, ten_phuong_tien, nam_sx, van_toc_toi_da):
        if not isinstance(hang_sx, str):
            raise TypeError("hang_sx phải là string")
        if not isinstance(ten_phuong_tien, str):
            raise TypeError("ten_phuong_tien phải là string")
        if not isinstance(nam_sx, int):
            raise TypeError("nam_sx phải là int")
        if not isinstance(van_toc_toi_da, float):
            raise TypeError("van_toc_toi_da phải là float")

        self.Hang_sx = hang_sx
        self.ten_phuong_tien = ten_phuong_tien
        self.nam_sx = nam_sx
        self.van_toc_toi_da = van_toc_toi_da

    def lay_thong_tin(self):
        return [self.Hang_sx, self.ten_phuong_tien,
                self.nam_sx, self.van_toc_toi_da]

    def __str__(self):
        return f'{self.Hang_sx},{self.ten_phuong_tien},{self.nam_sx},{self.van_toc_toi_da}'

    def descriptors(self):
        return 'Hang_sx,ten_phuong_tien,nam_sx,van_toc_toi_da'