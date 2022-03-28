import json
from django.http import HttpResponse


class BaseHttpResponse:
    def __init__(self, code, messageEn, messageAr, dic={}):
        self.code = code
        self.messageEn = messageEn
        self.messageAr = messageAr
        self.dic = dic

    def get_dic_object(self):
        return {"Code": int(self.code), 'MessageEn': self.messageEn, "MessageAr": self.messageAr}

    def get_compose_json(self):
        if type(self.dic) is list:
            data = self.dic
            regularMessage = json.dumps({**self.get_dic_object(), "Data": data})
            return regularMessage

        return json.dumps({**self.get_dic_object(), **self.dic})


def base_response(baseHttpResponse):
    return HttpResponse(baseHttpResponse.get_compose_json(), status=baseHttpResponse.code,
                        content_type='application/json')


def bad_request():
    baseHttpResponse = BaseHttpResponse(400, "Bad Request", "عفوا خطا في الطلب")
    return base_response(baseHttpResponse)


def rejected_login():
    return base_response(BaseHttpResponse("401", "Wrong Username or Password try again", "عفوا يوجد خطا في اسم المستخدم او كلمة السر"))


def un_authorized():
    return base_response(
        BaseHttpResponse("401", "UnAuthorized, or Session Ended .. Login Again",
                         "عفوا غير مسجل الدخول يرجى محاول تسجيل الدخول"))
