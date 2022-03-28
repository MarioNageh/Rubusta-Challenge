import os
from datetime import timedelta

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
