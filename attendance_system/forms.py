from django import forms
from .models import  Employee, EmployeeAttendance
from django.core.exceptions import ValidationError
from django.forms import BaseFormSet


DEPARTMENT_CHOICES = (
    ('A', 'All'),
    ('D','Development'),
    ('T', 'Testing'),
    ('H', 'HR')
)

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'phone_number', 'department']
        widgets = {
            'name' : forms.TextInput(attrs={ 
                'class': 'form-control',
                'placeholder': 'Employee Name'
                }),
            'email' : forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Employee Email',
            }),
             'phone_number' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Employee Phone number',
            }),
             'department' : forms.Select(attrs={
                'class': 'form-control'
            })
        }


# Validation for checking if each employee's attendace has been filled or not
class BaseAttendanceFormSet(BaseFormSet):
    def clean(self):
        for form in self.forms:
            record = form.cleaned_data.get('is_present')
            if record is None:
                raise ValidationError("Please enter every employees attendance")
    

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = EmployeeAttendance
        widgets = {'employee' : forms.HiddenInput, 'is_present': forms.Select(attrs={ 
            'class' : 'custom-select'
        })}
        fields = ('employee','is_present')

# Formset for displaying attendace form for all exsting employees
AttendanceFormset = forms.formset_factory(form= AttendanceForm, formset=BaseAttendanceFormSet, extra=0)


# For fetching attendance details within a date range
class AttendanceSearchForm(forms.Form):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control',}), required=True)
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control',}),required=True) 


# For filtering employees using either email or department or both
class EmployeeSearchForm(forms.Form):
    email = forms.EmailField(widget = forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Employee Email',
    }), required=False)
    departments = forms.TypedChoiceField(choices=DEPARTMENT_CHOICES,widget=forms.Select(attrs={
        'class' : 'custom-select'
    }))