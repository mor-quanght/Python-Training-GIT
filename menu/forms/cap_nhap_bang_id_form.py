from django import forms


class Cap_nhap_bang_id(forms.Form):
    id = forms.IntegerField()
    ten = forms.CharField(max_length=100)

    gioitinh = (
        ('Nam', 'Nam'),
        ('Nu', 'Nu'),
    )
    hocluc = (
        ('Gioi', 'Gioi'),
        ('Kha', 'Kha'),
        ('TrungBinh', 'TrungBinh'),
        ('Kem', 'Kem'),
    )
    gioi_tinh = forms.ChoiceField(choices=gioitinh)
    tuoi = forms.IntegerField()
    diem_toan = forms.IntegerField()
    diem_ly = forms.IntegerField()
    diem_hoa = forms.IntegerField()
