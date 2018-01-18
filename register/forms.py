from django import forms
class RegisterForm(forms.Form):
    username=forms.CharField(label="username",max_length=100,required='false',widget=forms.TextInput(attrs={'class':'form-control'}))
    firstname=forms.CharField(label="firstname",max_length=100,required='false',widget=forms.TextInput(attrs={'class':'form-control'}))
    lastname=forms.CharField(label="lastname",max_length=100,required='false',widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label="Password",max_length=100,required='false',  widget=forms.PasswordInput(attrs={'placeholder': '*******','class':'form-control'}))
    email=forms.CharField(label="Email",required='false',max_length=200,  widget=forms.TextInput(attrs={'placeholder': 'xyz@gmail.com','class':'form-control'}))
  

class LoginForm(forms.Form):
    login_username=forms.CharField(label="username",max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    login_password=forms.CharField(label="Password",max_length=100,  widget=forms.PasswordInput(attrs={'placeholder': '*******','class':'form-control'}))