# Trang đăng ký
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render
# views.py (cập nhật với REST API)
from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

# View đăng ký người dùng
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Lưu người dùng mới vào cơ sở dữ liệu
            return redirect('login')  # Điều hướng đến trang đăng nhập
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

# View đăng nhập người dùng
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('employee_list')  # Điều hướng đến trang chủ sau khi đăng nhập
            else:
                form.add_error(None, 'Sai email hoặc mật khẩu')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def employee_page(request):
    return render(request, 'accounts/employee.html')

# Tạo ViewSet cho Employee
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# API để lấy danh sách nhân viên
@api_view(['GET'])
def employee_list(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_employee(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return Response(status=404)

    serializer = EmployeeSerializer(employee)
    return Response(serializer.data)

# API để thêm nhân viên
@api_view(['POST'])
def add_employee(request):
    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API để sửa thông tin nhân viên
@api_view(['PUT'])
def update_employee(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return Response({'success': False}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'data': serializer.data})
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# API để xóa nhân viên
@api_view(['DELETE'])
def delete_employee(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






