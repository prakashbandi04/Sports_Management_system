from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo
from datetimepicker.widgets import DateTimePicker
class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','email','password')
class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portofolio_site','profile_pic','country','sport')
class availform(forms.Form):
    check_in = forms.DateTimeField(required=True,input_formats=['%Y-%m-%d %H:%M',])
    check_out = forms.DateTimeField(required=True,input_formats=['%Y-%m-%d %H:%M',])
