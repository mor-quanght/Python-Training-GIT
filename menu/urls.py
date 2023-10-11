
from django.contrib import admin
from django.urls import path,include
from menu import views



urlpatterns = [
    path('', views.my_menu,name='menu'),
    path('them_sinh_vien',views.them_sinh_vien,name='them_sinh_vien'),
    path('cap_nhap_bang_id', views.cap_nhap_bang_id, name='cap_nhap_bang_id'),
    path('xoa_bang_id', views.xoa_bang_id, name='xoa_bang_id'),
    path('tim_kiem_bang_ten', views.tim_kiem_bang_ten, name='tim_kiem_bang_ten'),
    path('sap_xep/<str:field>/<str:order>', views.sap_xep, name='sap_xep'),
    path('hien_thi', views.hien_thi, name='hien_thi'),
]
