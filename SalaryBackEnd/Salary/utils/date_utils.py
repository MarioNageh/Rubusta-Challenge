import datetime
from dateutil.relativedelta import relativedelta

DAY_OF_WEEK = {
    "MONDAY": 0,
    "TUESDAY": 1,
    "WEDNESDAY": 2,
    "THURSDAY": 3,
    "FRIDAY": 4,
    "SATURDAY": 5,
    "SUNDAY": 6
}

WEEK_ENDS = [DAY_OF_WEEK["FRIDAY"], DAY_OF_WEEK["SATURDAY"]]


def get_date_by_month_year(month, year):
    # For 05 Month
    corrected_month = f"0{month}" if len(month) == 1 else month
    date = f'{year}-{corrected_month}-01 00:00:00'
    return datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    # print(datem.strftime("%A"))
    # print(last_day_of_month(datem).strftime("%A"))
    # print(mid_day_of_month(datem).strftime("%A"))
    # print(mid_day_of_month(datem))
    # print(mid_day_of_month(datem).weekday())

def get_month_name(month, year):
    date = get_date_by_month_year(month, year)
    return date.strftime('%B')

def get_day_number(month, year,func):
    date = get_date_by_month_year(month, year)
    day = func(date)
    while day.weekday() in WEEK_ENDS:
        day= day - datetime.timedelta(days=1)
    return day.strftime("%d")

def get_bonus_day_number(month, year):
    date = get_date_by_month_year(month, year)
    mid_day = mid_day_of_month(date)
    while mid_day.weekday() in WEEK_ENDS:
        mid_day= mid_day - datetime.timedelta(days=1)

    # print(mid_day)
    # print(mid_day.strftime("%A"))
    return mid_day.strftime("%d")


def last_day_of_month(date):
    return date.replace(day=1) + relativedelta(months=1) - relativedelta(days=1)


def mid_day_of_month(date):
    return date.replace(day=1) + relativedelta(days=14)
