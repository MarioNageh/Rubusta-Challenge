from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from Salary.models import Admins
from Salary.utils.authUtils import hashSha1
from Salary.utils.http_responses import *


# Create your tests here.


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
