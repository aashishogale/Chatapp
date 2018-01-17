from django import forms
class RegisterForm(forms.Form):
    username=forms.CharField(label="Name",max_length=100)
    firstname=forms.CharField(label="firstname",max_length=100)
    lastname=forms.CharField(label="lastname",max_length=100)
    password=forms.CharField(label="Password",max_length=100)
