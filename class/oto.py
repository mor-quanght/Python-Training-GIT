from phuong_tien_giao_thong import PhuongTienGiaoThong


class Oto(PhuongTienGiaoThong):
    def __init__(self, hang_sx, ten_phuong_tien, nam_sx, van_toc_toi_da, so_cho_ngoi, so_banh, dong_co):
        super().__init__(hang_sx, ten_phuong_tien, nam_sx, van_toc_toi_da)
        if not isinstance(so_cho_ngoi, int):
            raise TypeError("so_cho_ngoi phải là int")
        if not isinstance(so_banh, int):
            raise TypeError("so_banh phải là int")
        if not isinstance(dong_co, str):
            raise TypeError("dong_co phải là string")

        self.so_cho_ngoi = so_cho_ngoi
        self.so_banh = so_banh
        self.dong_co = dong_co

    def huy_bo(self):
        super().nhap_thong_tin('', '', 0, 0.0)
        self.so_cho_ngoi = 0
        self.so_banh = 0
        self.dong_co = ''

    def input(self, hang_sx, ten_phuong_tien, nam_sx, van_toc_toi_da, so_cho_ngoi, so_banh, dong_co):
        if not isinstance(hang_sx, str):
            raise TypeError("hang_sx phải là string")
        if not isinstance(ten_phuong_tien, str):
            raise TypeError("ten_phuong_tien phải là string")
        if not isinstance(nam_sx, int):
            raise TypeError("nam_sx phải là int")
        if not isinstance(van_toc_toi_da, float):
            raise TypeError("van_toc_toi_da phải là float")

        super().nhap_thong_in(hang_sx, ten_phuong_tien, nam_sx, van_toc_toi_da)
        self.so_cho_ngoi = so_cho_ngoi
        self.so_banh = so_banh
        self.dong_co = dong_co

    def van_toc_cs(self):
        return self.van_toc_toi_da / self.so_banh

    def __lt__(self, other):
        return self.van_toc_cs() < other.van_toc_cs()

    def lay_thong_tin(self):
        data=super().lay_thong_tin()
        data.append(self.so_cho_ngoi)
        data.append(self.so_banh)
        data.append(self.dong_co)
        return data

    def __str__(self):
        string=super().__str__()
        string += f',{self.so_cho_ngoi},{self.so_banh},{self.dong_co},{self.van_toc_cs()}'
        return string

    def descriptors(self):
        string=super().descriptors()
        string += ',so_cho_ngoi,so_banh,dong_co,van_toc_co_so'
        return string
