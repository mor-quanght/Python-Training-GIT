from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from django.db.models import F


# Create your models here.


class Sinhvien(models.Model):
    ten = models.CharField(max_length=100)

    class gioitinh(models.TextChoices):
        Nam = 'Nam'
        Nu = 'Nu'

    class hocluc(models.TextChoices):
        Gioi = 'Gioi'
        Kha = 'Kha'
        TrungBinh = 'TrungBinh'
        Kem = 'Kem'

    gioi_tinh = models.CharField(choices=gioitinh.choices, max_length=5)
    tuoi = models.SmallIntegerField()
    diem_toan = models.SmallIntegerField()
    diem_ly = models.SmallIntegerField()
    diem_hoa = models.SmallIntegerField()
    diem_tb = models.SmallIntegerField()
    hoc_luc = models.CharField(choices=hocluc.choices, max_length=20)

    def __str__(self):
        return f'{self.ten},{self.gioi_tinh},{self.tuoi},{self.diem_toan},{self.diem_ly},{self.diem_hoa},{self.diem_tb},{self.hocluc}'

