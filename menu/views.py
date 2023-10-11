from django.shortcuts import render
from .forms.them_sinh_vien_form import Sinhvienform
from .forms.cap_nhap_bang_id_form import Cap_nhap_bang_id
from .forms.xoa_sv_form import Xoa_bang_id
from .forms.tim_kiem_theo_ten import Tim_kiem_theo_ten


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
            sinhvien.save()
            return HttpResponseRedirect('/my_menu/')

    else:
        sv_form = Sinhvienform()

    return render(reqest, 'them_sinh_vien.html', {"form": sv_form})


def cap_nhap_bang_id(reqest):
    if reqest.method == 'POST':
        cap_nhap_form = Cap_nhap_bang_id(reqest.POST)
        if cap_nhap_form.is_valid():
            diemtb = tinh_diemtb(cap_nhap_form.cleaned_data['diem_toan'],
                                 cap_nhap_form.cleaned_data['diem_ly'],
                                 cap_nhap_form.cleaned_data['diem_hoa'])

            hocluc = tinh_hoc_luc(diemtb)

            sinhvien = Sinhvien(id=cap_nhap_form.cleaned_data['id'],ten=cap_nhap_form.cleaned_data['ten'],
                                gioi_tinh=cap_nhap_form.cleaned_data['gioi_tinh'],tuoi=cap_nhap_form.cleaned_data['tuoi'],
                                diem_toan=cap_nhap_form.cleaned_data['diem_toan'],diem_ly=cap_nhap_form.cleaned_data['diem_ly'],
                                diem_hoa=cap_nhap_form.cleaned_data['diem_hoa'],diem_tb=diemtb, hoc_luc=hocluc)

            sv_by_id=Sinhvien.objects.filter(id=cap_nhap_form.cleaned_data['id'])
            sv_by_id=sinhvien
            sv_by_id.save()
            return HttpResponseRedirect('/my_menu/')

    else:
        cap_nhap_form = Cap_nhap_bang_id()

    return render(reqest, 'cap_nhap_bang_id.html', {"form": cap_nhap_form})


def xoa_bang_id(reqest):
    if reqest.method == 'POST':
        xoa_bang_form = Xoa_bang_id(reqest.POST)
        if xoa_bang_form.is_valid():
            sv_by_id=Sinhvien.objects.filter(id=xoa_bang_form.cleaned_data['id'])
            sv_by_id.delete()
            return HttpResponseRedirect('/my_menu/')

    else:
        xoa_bang_form = Xoa_bang_id()

    return render(reqest,'xoa_bang_id.html',{'form': xoa_bang_form})


def tim_kiem_bang_ten(reqest):
    if reqest.method == 'POST':
        tim_kiem_theo_ten = Tim_kiem_theo_ten(reqest.POST)
        if tim_kiem_theo_ten.is_valid():
            danhsach_sv=[]
            sv_by_id = Sinhvien.objects.filter(ten__icontains=tim_kiem_theo_ten.cleaned_data['ten'])
            return render(reqest, 'hien_thi.html', { 'danhsach_sv': sv_by_id  })

    else:
        tim_kiem_theo_ten = Tim_kiem_theo_ten()

    return render(reqest, 'tim_kiem_sv.html', {'form': tim_kiem_theo_ten})


def sap_xep(reqest,field,order):
    if order=='asc':
        danhsach_sv = Sinhvien.objects.all().order_by(field).values()
    else:
        danhsach_sv = Sinhvien.objects.all().order_by('-'+field).values()

    return render(reqest,'hien_thi.html',{'danhsach_sv':danhsach_sv})


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
