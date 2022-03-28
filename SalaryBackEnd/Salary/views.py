from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from Salary.models import Admins, Employee
from Salary.utils.authUtils import hashSha1
from Salary.utils.date_utils import get_date_by_month_year, get_bonus_day_number, get_day_number, mid_day_of_month, \
    last_day_of_month, get_month_name
from Salary.utils.http_responses import *


# Create your tests here.


@require_http_methods(["GET"])
def salary(request):
    month = None
    year = None
    try:
        month = request.GET['month']
        year = request.GET['year']
    except:
        return base_response(BaseHttpResponse(403, "You Must Determine Month,Year", "يجب تحديد الشهر والعام"))

    try:
        day_of_bonus = get_day_number(month, year, mid_day_of_month)
        day_of_salary = get_day_number(month, year, last_day_of_month)
        month_name = get_month_name(month, year)
    except:
        return base_response(
            BaseHttpResponse(403, "You Must Pass Invalid Month,Year", "يجب ان يكون الشهر و السنة صحيح"))

    total_salaries = 0
    employees = Employee.objects.filter(is_active=True, is_deleted=False)
    for x in employees:
        total_salaries += x.baseSalary

    total_bonus = total_salaries * .1

    return_dic = {
        "Month": month_name,
        "Salaries_payment_day": day_of_salary,
        "Bonus_payment_day": day_of_bonus,
        "Salaries_total": f"${total_salaries}",
        "Bonus_total": f"${total_bonus}",
        "Payments_total": f"${total_salaries + total_bonus}"
    }

    return base_response(BaseHttpResponse(200, "Successful Generated Report", "تم نجهيز التقرير بنجاح", return_dic))


@require_http_methods(["POST"])
def login(request):
    try:
        # Form Data
        requestBody = request.POST
        email = requestBody["email"]
        password = requestBody["password"]
        if not email or not password:
            return bad_request()

        # Direct Sign In
        admin = Admins.objects.filter(email=email, password=hashSha1(password))
        if admin:
            admin = admin.first()
            return admin.login(request)
        else:
            return rejected_login()
    except BaseException as a:
        print(a)
        return bad_request()
