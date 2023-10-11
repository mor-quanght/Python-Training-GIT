from django.shortcuts import render
from .forms.them_sinh_vien_form import Sinhvienform
from django.http import HttpResponseRedirect
from .models import Sinhvien


# Create your views here.
def my_menu(request):
    return render(request, 'menu.html')


def them_sinh_vien(reqest):
    if reqest.method == 'POST':
        sv_form = Sinhvienform(reqest.POST)
        if sv_form.is_valid():
            diemtb = tinh_diemtb(sv_form.cleaned_data['diem_toan'],
                                 sv_form.cleaned_data['diem_ly'],
                                 sv_form.cleaned_data['diem_hoa'])

            hocluc = tinh_hoc_luc(diemtb)

            sinhvien = Sinhvien(ten=sv_form.cleaned_data['ten'], gioi_tinh=sv_form.cleaned_data['gioi_tinh'],
                                tuoi=sv_form.cleaned_data['tuoi'], diem_toan=sv_form.cleaned_data['diem_toan'],
                                diem_ly=sv_form.cleaned_data['diem_ly'], diem_hoa=sv_form.cleaned_data['diem_hoa'],
                                diem_tb=diemtb, hoc_luc=hocluc)
            '''
            Sinhvien.ten = sv_form.cleaned_data['ten']
            Sinhvien.gioitinh = sv_form.cleaned_data['gioi_tinh']
            Sinhvien.tuoi = sv_form.cleaned_data['tuoi']
            Sinhvien.diem_toan = sv_form.cleaned_data['diem_toan']
            Sinhvien.diem_ly = sv_form.cleaned_data['diem_ly']
            Sinhvien.diem_hoa = sv_form.cleaned_data['diem_hoa']
            Sinhvien.diem_tb = (Sinhvien.diem_ly + Sinhvien.diem_toan + Sinhvien.diem_hoa) / 3
            Sinhvien.hoc_luc = tinh_hoc_luc(Sinhvien.diem_tb)'''
            sinhvien.save()
            return HttpResponseRedirect('/my_menu/')
    else:
        sv_form = Sinhvienform()

    return render(reqest, 'them_sinh_vien.html', {"form": sv_form})


def cap_nhap_bang_id(reqest):
    pass


def xoa_bang_id(reqest):
    pass


def tim_kiem_bang_ten(reqest):
    pass


def sap_xep(reqest):
    pass


def hien_thi(reqest):
    danhsach_sv=Sinhvien.objects.all().values()
    return render(reqest,'hien_thi.html',{'danhsach_sv':danhsach_sv})

def tinh_hoc_luc(diemtb):
    if diemtb >= 8:
        return 'Gioi'
    elif diemtb >= 6.5:
        return 'Kha'
    elif diemtb >= 5:
        return 'TrungBinh'
    else:
        return 'Kem'


def tinh_diemtb(diem_toan, diem_ly, diem_hoa):
    return (diem_ly + diem_hoa + diem_toan) / 3
