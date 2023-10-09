from oto import Oto


sort_dict={}
'''
def sort_danh_sach(danh_sach_oto):
    length = len(danh_sach_oto)
    danh_sach_moi = []
    id1 = 0
    id2 = 0

    while id1 < length:
        id2 = id1 + 1
        while id2 < length:



    return danh_sach_oto
'''

def hien_thi(danh_sach_oto):
    for oto in danh_sach_oto:
        sort_dict[oto] = oto.van_toc_cs()
    danh_sach_oto=sorted(sort_dict.items(),key=lambda x:x[1],reverse=True)

    for oto in danh_sach_oto:
        print(oto[0])