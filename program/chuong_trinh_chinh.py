from nhap_ptgt import nhap_ptgt
from nhap_n_oto import nhap_n_oto
from hien_thi_thong_tin import hien_thi
from oto import Oto


# Nhap phuong tien giao thong
def nhap_du_lieu_ptgt():
    return nhap_ptgt()


    # Hien thi thong tin
def hienthi_ptgt(ptgt):
    print(ptgt.descriptors())
    print(ptgt)


# Nhap thong tin Oto
def nhap_oto():
    danh_sach_oto=[]
    danh_sach_oto = nhap_n_oto()
    return danh_sach_oto

# Hien thi thong tin Oto
def hien_thi_oto(danh_sach_oto):
    print(danh_sach_oto[0].descriptors())
    for oto in danh_sach_oto:
        print(oto)


def sapxep_oto(danh_sach_oto):
    print(danh_sach_oto[0].descriptors())
    hien_thi(danh_sach_oto)


#nhap_hienthi_ptgt()
#nhap_hien_thi_oto()





def menu_interface():
    ptgt=''
    ds_oto=''
    while True:
        print('''Chương trình chính:  
        0. Thoát
        1. Nhập từ bàn phím thông tin của một phương tiện giao thông 
        PhuongTienGiaoThong. 
        2. Hiển thị thông tin của phương tiện giao thông vừa nhập ra màn hình.  
        3. Nhập thông tin cho n đối tượng OTO bao gồm: Hãng sản xuất, Tên phương tiện, Năm sản xuất, Vận tốc tối đa, số chỗ ngồi, kiểu động cơ. 
        4. In ra màn hình thông tin của n đối tượng OTO cùng với vận tốc cơ sở. 
        5. Sắp xếp danh sách các đối tượng OTO theo thứ tự giảm dần của Vận tốc tối đa.''')
        error_string = 'Không có chức năng tương ứng với số vừa nhập. Vui lòng nhập lại các số trong menu'
        menu_input = int(input(">"))

        if menu_input==0:
            break
        elif menu_input==1:
            ptgt=nhap_ptgt()
        elif menu_input==2:
            hienthi_ptgt(ptgt)
        elif menu_input==3:
            ds_oto=nhap_n_oto()
        elif menu_input==4:
            hien_thi_oto(ds_oto)
        elif menu_input==5:
            sapxep_oto(ds_oto)
        else:
            print(error_string)

menu_interface()

