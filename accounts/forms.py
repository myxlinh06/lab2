from django import forms
from .models import CustomUser

# Form đăng ký người dùng
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # Trường mật khẩu

    class Meta:
        model = CustomUser  # Chỉ định model là CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password']  # Các trường cần nhập

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Mã hóa mật khẩu
        if commit:
            user.save()  # Lưu người dùng vào cơ sở dữ liệu
        return user

# Form đăng nhập
class LoginForm(forms.Form):
    email = forms.EmailField()  # Trường email
    password = forms.CharField(widget=forms.PasswordInput)  # Trường mật khẩu

# forms thông tin
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'phone', 'department', 'hire_date']
