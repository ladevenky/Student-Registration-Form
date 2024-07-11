
from django import forms


class StudForm(forms.Form):
    s_name = forms.CharField(max_length=30,label='Student name')
    s_class = forms.CharField(max_length=30,label='Class')
    s_addr = forms.CharField(max_length=30,label='Address')
    s_school = forms.CharField(max_length=30,label='School Nmae')
    s_email = forms.EmailField(max_length=30,label='Student E-Mail')


class Sform(forms.Form):
    s_name = forms.CharField(max_length=30,label='Student name')