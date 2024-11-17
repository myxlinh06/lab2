# accounts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'employees', views.EmployeeViewSet)

urlpatterns = [

    path('register/', views.register, name='register'),  # Đường dẫn trang đăng ký
    path('login/', views.login_view, name='login'),      # Đường dẫn trang đăng nhập
    path('employees-list/', views.employee_page, name='employee_list'),

    # API endpoints
    path('api/employees/', views.employee_list, name='api_employee_list'),
    path('api/employees/create/', views.add_employee, name='api_employee_add'),
    path('api/employees/<int:id>/', views.get_employee, name='api_employee_detail'),
    path('api/employees/<int:id>/update/', views.update_employee, name='api_employee_update'),
    path('api/employees/<int:id>/delete/', views.delete_employee, name='api_employee_delete'),

]


