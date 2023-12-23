from django import forms
from django.core.validators import FileExtensionValidator

class RegisterClient(forms.Form):
    username = forms.CharField(max_length=200, label="Username:")
    password = forms.CharField(widget = forms.PasswordInput())
    email =forms.EmailField(max_length=200, label="Email:")

class EmailVerification(forms.Form):
    four_digit_code = forms.IntegerField(label="Verification Code: ") 

class LoginPage(forms.Form):
    username = forms.CharField(max_length=200, label="Username:")
    password = forms.CharField(widget = forms.PasswordInput())

class UploadFile(forms.Form):
    file = forms.FileField(validators=[FileExtensionValidator(['pptx', 'docx', 'xlsx'])])