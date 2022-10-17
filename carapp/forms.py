from django import forms
from .models import*


class registerform(forms.ModelForm):
    class Meta:
        model=registermodel
        fields=('firstname','middlename','lastname','address','phone','gender','email','psw')
        widigets={
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'middlename':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'psw':forms.TextInput(attrs={'class':'form-control'}),
            # 'img':forms.TextInput(attrs={'class':'form-control'}),


 }


class bookingform(forms.ModelForm):
    class Meta:
        model=bookingmodel
        fields=('name','vehiclename','price','booking','phone','address')
        widigets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'vehiclename':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'booking':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),

            }
