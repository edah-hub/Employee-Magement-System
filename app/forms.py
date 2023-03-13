from django import forms
from django import forms
from .models import Employee

# This is for employee
class EmployeeRegistrationForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        class EmployeeRegistrationForm(forms.ModelForm):
         class Meta:
            model = Employee
            fields = "__all__"