from django.urls import path
from . views import (
    edit_today_attendance,
    employee_delete,
    employee_update,
    employees_listing, 
    view_today_attendance,
    employee_attendance_details,
    employee_create
)
app_name = 'attendance_system'

urlpatterns = [
    path('', employees_listing, name='all_attendance_dashboard'),
    path('view-today-attendance/', view_today_attendance, name='view_today_attendance'),
    path('edit-today-attendance/', edit_today_attendance, name='edit_today_attendance'),
    path('employee-attendance-details/<empid>/', employee_attendance_details, name='employee_attendance_details'),
    path('employee-create/', employee_create, name='employee_create'),
    path('employee-update/<empid>/', employee_update, name='employee_update'),
    path('employee-delete/<empid>/', employee_delete, name='employee_delete')
]
