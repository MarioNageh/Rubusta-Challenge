import json

from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import datetime


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
