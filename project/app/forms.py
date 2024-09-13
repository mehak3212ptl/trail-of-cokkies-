
from django import forms
class RegistrationForm(forms.Form):
    stu_name = forms.CharField()
    stu_email = forms.EmailField()
    # stu_name=forms.TextInput()
    # stu_email= forms.EmailInput()
    # stu_city=forms.TextInput()
    # stu_mobile=forms.NumberInput()
    # class Meta:      
    #     fields = ('stu_name', 'stu_email', 'stu_city', 'stu_mobile', 'stu_password')
    #     widgets = {
    #         'stu_name': forms.TextInput(attrs={'class': 'form-control'}),
    #         'stu_email': forms.EmailInput(attrs={'class': 'form-control'}),
    #         'stu_city': forms.TextInput(attrs={'class': 'form-control'}),
    #         'stu_mobile': forms.NumberInput(attrs={'class': 'form-control'}),
    #         'stu_password': forms.PasswordInput(attrs={'class': 'form-control'}),
    #     }