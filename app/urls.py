from django.urls import path
from .views import home,register_employee,employee_list,employee_profile,editemp
from django.urls import reverse


urlpatterns = [
    path("",home,name="home"),
    path("register/",register_employee,name="register_employee"),
    path("list/",employee_list,name="employee_list"),
    path("profile/<int:id>/",employee_profile,name="employee_profile"),
    path("edit/<int:id>/",editemp,name="edit_employee"),
]