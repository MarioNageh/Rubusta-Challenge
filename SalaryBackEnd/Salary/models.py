import json

from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import datetime

from Salary.utils.authUtils import generateAuthToken
from Salary.utils.http_responses import *
from Salary.utils.network import get_client_ip


class BaseModel(models.Model):
    creation_time = models.DateTimeField(auto_now_add=True, db_column="TimeCreated")
    is_active = models.BooleanField(default=True, db_column="IsActive")
    activated_time = models.DateTimeField(null=True, blank=True, db_column='TimeActivated')
    is_deleted = models.BooleanField(default=False, db_column='IsDeleted')
    deleted_time = models.DateTimeField(null=True, blank=True, db_column='TimeDeleted')

    class Meta:
        abstract = True


class Admins(BaseModel):
    idAdmin = models.AutoField(primary_key=True, db_column='IdAdmin')
    firstName = models.CharField(null=False, max_length=50, blank=False, db_column="FirstName")
    lastName = models.CharField(null=False, max_length=50, blank=False, db_column="LastName")
    email = models.CharField(null=False, max_length=50, blank=False, unique=True, db_column="Email")
    password = models.CharField(null=False, max_length=50, blank=False, db_column="Password")
    phone = models.CharField(null=False, max_length=50, blank=False, db_column="Phone")

    is_suspended = models.BooleanField(default=False, db_column="IsSuspended")
    suspended_time = models.DateTimeField(null=True, blank=True, db_column='TimeSuspended')
    suspended_reason = models.CharField(max_length=100, null=True, blank=True, db_column="SuspendedReason")

    lastSeen = models.DateTimeField(null=True, blank=True, db_column='LastSeen')
    lastActivity = models.TextField(db_column='LastActivity')

    class Meta:
        db_table = "Admin"

    def updateLastSeenActivity(self, request):
        from django.urls import resolve
        routeName = resolve(request.path_info).url_name
        requestBody = None
        try:
            requestBody = request.body
        except:
            requestBody = ""

        self.lastActivity = json.dumps({
            "LastCalledApi": routeName,
            "RequestMethod": request.method,
            # "RequestBody": str(requestBody),
            "RequestDevice": request.META['HTTP_USER_AGENT'],
            "RequestIP": get_client_ip(request)
        })
        request.messageBody = requestBody
        self.lastSeen = datetime.today()
        self.save()

    def login(self, request):
        messageAR = "تم تسجيل الدخول بنجاح"
        messageEN = "Successful Login"
        if self.is_active and not self.is_suspended and not self.is_deleted:
            self.updateLastSeenActivity(request)
            token = generateAuthToken(self)
            return base_response(BaseHttpResponse(200, messageEN, messageAR, {"Token": token}))

        elif not self.is_active:
            return base_response(BaseHttpResponse(401, "Account Not Activated", "لم يتم تفعيل الحساب"))
            # Account Not Activated
        elif self.is_suspended:
            return base_response(BaseHttpResponse(401, "Account Suspended", "الحساب معلق"))
            # Account Is Suspended
        elif self.is_deleted:
            return base_response(
                BaseHttpResponse(401, "Account Has Deleted From Our Servers", "تم حذف الحساب من النظام"))
            # Account Is Deleted From Our Servers


class Department(BaseModel):
    class Meta:
        db_table = "Department"

    idDepartment = models.AutoField(primary_key=True, db_column='IdDepartment')
    departmentNameAr = models.CharField(max_length=255, null=False, blank=False, db_column="DepartmentNameAr")
    departmentNameEn = models.CharField(max_length=255, null=False, blank=False, db_column="DepartmentNameEn")


class Employee(BaseModel):
    class Meta:
        db_table = "Employee"

    idEmployee = models.AutoField(primary_key=True, db_column='IdEmployee')
    firstName = models.CharField(null=False, max_length=50, blank=False, db_column="FirstName")
    lastName = models.CharField(null=False, max_length=50, blank=False, db_column="LastName")
    nationalId = models.CharField(null=False, max_length=14, blank=False, db_column="NationalId")
    phone = models.CharField(null=False, max_length=50, blank=False, db_column="Phone")
    email = models.CharField(null=False, max_length=50, blank=False, unique=True, db_column="Email")
    address = models.CharField(max_length=50, null=False, blank=False, default="{Rubusta}")
    baseSalary = models.FloatField(max_length=50, null=False, blank=False, db_column='BaseSalary')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, db_column="IdDepartment")


class SalaryLog(BaseModel):
    class Meta:
        db_table = "SalaryLog"

    idSalaryLog = models.AutoField(primary_key=True, db_column='idSalaryLog')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column="IdEmployee")
    previousBaseSalary = models.FloatField(max_length=50, null=False, blank=False, db_column='PreviousBaseSalary')
    BaseSalary = models.FloatField(max_length=50, null=False, blank=False, db_column='BaseSalary')
