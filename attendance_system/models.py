from django.db import models
from django.core.validators import RegexValidator
from django.db.models.signals import pre_save
import datetime


# Create your models here.

DEPARTMENT_CHOICES = (
    ('D','Development'),
    ('T', 'Testing'),
    ('H', 'HR')
)

ATTENDANCE_CHOICES = (
    ('absent', 'Absent'),
    ('present', 'Present')
)

# Name validator, it only accept alphabets with space in 2 words
name_regex = RegexValidator(regex=r'^[a-zA-Z-,]+(\s{0,1}[a-zA-Z-, ])*$', message="Employee name must be valid")

# Phone number validator
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
   
class Employee(models.Model):
    name= models.CharField(max_length=50, null=False, blank=False, validators=[name_regex])
    email = models.EmailField(null=False,blank=False,unique=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False,null=False, unique=True) # validators should be a list
    department = models.CharField(choices=DEPARTMENT_CHOICES, max_length=1, null=False, blank=False)

    def __str__(self):
        return f"{self.name} - {self.get_department_display()}"


class EmployeeAttendance(models.Model):
    employee = models.ForeignKey('Employee',on_delete=models.CASCADE, null=False, blank=False)
    is_present = models.CharField(max_length=8, choices=ATTENDANCE_CHOICES, blank=False,null=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self) :
        return f"{self.employee.name} {self.date}"
    

# Below pre_save signal is used to avoid duplicate employee attendance entries on any particular day, 
# if attendace details exists for any employee on that particular date 
# and if tried to add a new attendance record for same employee through admin panel then 
# instead of creating a new record within table it will update the existing record.

def pre_save_function_employee_attendance(sender,instance, **kwargs):
    record = EmployeeAttendance.objects.filter(employee__id= instance.employee.id, date=instance.date)
    if record.exists():
        record.delete()
        instance.save()


pre_save.connect(pre_save_function_employee_attendance, sender=EmployeeAttendance)
      



