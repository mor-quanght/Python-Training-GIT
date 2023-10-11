
from django import forms


class Tim_kiem_theo_ten(forms.Form):
    ten = forms.CharField(max_length=100)

