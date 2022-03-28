import os
from datetime import timedelta
from random import randrange

import django

from Salary.utils.authUtils import hashSha1

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SalaryBackEnd.settings")
django.setup()

from Salary.models import *

admins = Admins.objects.all()
if len(admins) <= 0:
    admin = Admins(firstName="Rubusta", lastName="Admin", email="Admin@Rubusta.com", password=hashSha1("1234")
                   , phone="01208847854")
    admin.save()

deparments = Department.objects.all()
if len(deparments) <= 0:
    deparment = Department(departmentNameAr="قسم البرمجيات", departmentNameEn="Programming")
    deparment.save()

employee = Employee.objects.all()
if len(employee) <= 0:
    for i in range(5):
        employee_fake = Employee(firstName=f"Employee {i}", lastName="Rubusta", email=f"{i}@Rubusta.com",
                                 nationalId=randrange(10000000000000, 19999999999999), phone="01208847854",
                                 address="Maadi", baseSalary=(i * i) + 2000, department_id=1)
        employee_fake.save()
