from them_sinh_vien import them_sinh_vien
from cap_nhap_bang_id import cap_nhap_bang_id
from xoa_bang_id import xoa_bang_id
from tim_kiem_theo_ten import tim_kiem_theo_ten
from sap_xep_sinh_vien import sap_xep_sinh_vien
from sinh_vien import Sinhvien

danh_sach_sv = []


def menu_interface():
    while True:
        print('''Chương trình chính:  
            0. Thoát
            1. Thêm sinh viên.
            2. Cập nhật thông tin sinh viên bởi ID.
            3. Xóa sinh viên bởi ID.
            4. Tìm kiếm sinh viên theo tên.
            5. Sắp xếp sinh viên theo điểm trung bình (GPA - tăng dần).
            6. Sắp xếp sinh viên theo tên tăng dần theo bảng chữ cái.
            7. Sắp xếp sinh viên theo ID giảm dần.
            8. Hiển thị danh sách sinh viên.''')
        error_string = 'Không có chức năng tương ứng với số vừa nhập. Vui lòng nhập lại các số trong menu'
        menu_input = int(input(">"))
        global  danh_sach_sv
        if menu_input == 0:
            exit()
        elif menu_input == 1:
            danh_sach_sv.append(them_sinh_vien())
        elif menu_input == 2:
            cap_nhap_bang_id(danh_sach_sv)
        elif menu_input == 3:
            xoa_bang_id(danh_sach_sv)
        elif menu_input == 4:
            tim_kiem_theo_ten(danh_sach_sv)
        elif menu_input == 5:
            danh_sach_sv=sap_xep_sinh_vien(danh_sach_sv, 'diem_tb', False)
        elif menu_input == 6:
            danh_sach_sv=sap_xep_sinh_vien(danh_sach_sv, 'ten', False)
        elif menu_input == 7:
            danh_sach_sv=sap_xep_sinh_vien(danh_sach_sv, 'id', True)
        elif menu_input == 8:
            if danh_sach_sv:
                sv = danh_sach_sv[0]
                sv.thuoc_tinh()
                for sinhvien in danh_sach_sv:
                    print(sinhvien)
            else:
                print('Chua nhap sinh vien')
        else:
            print(error_string)
menu_interface()
