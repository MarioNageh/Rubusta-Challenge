import base64
import hashlib
import hmac
from datetime import datetime

from django.urls import resolve
from django.utils.deprecation import MiddlewareMixin

from SalaryBackEnd.settings import SECRET_KEY_AUTH
from Salary.models import Admins
from Salary.utils.http_responses import *


class AuthMiddleWear(MiddlewareMixin):
    def get_route_name(self, request):
        return resolve(request.path_info).url_name

    def process_request(self, request):
        # Login Route Must Be UnAuth
        list_of_un_authorized_end_points = ['Login']
        # If This Route Not In AuthList We Will Check Keys
        if self.get_route_name(request) not in list_of_un_authorized_end_points:
            return self.check_auth_key(request)

    def check_auth_key(self, request):
        headerPartBase64 = payloadPartBase64 = signaturePart = None
        tokenPartCount = 0
        try:
            authHeader = request.META["HTTP_AUTHORIZATION"]
            authHeaderKey = authHeader[7:len(authHeader)]
            tokenPartCount = authHeaderKey.split(".")
            if len(tokenPartCount) != 3:
                return un_authorized()

            headerPartBase64 = tokenPartCount[0]
            payloadPartBase64 = tokenPartCount[1]
            signaturePart = tokenPartCount[2]
            headerPartBase64AndPayloadPart = f'{headerPartBase64}.{payloadPartBase64}'
            calculateMessageSignature = hmac.new(SECRET_KEY_AUTH.encode('utf-8'),
                                                 headerPartBase64AndPayloadPart.encode('utf-8'),
                                                 hashlib.sha256).hexdigest()

            if calculateMessageSignature != signaturePart:
                return un_authorized()

            decodedHeader = None
            decodedPayload = None
            try:
                decodedHeader = json.loads(base64.decodebytes(headerPartBase64.encode('utf-8')))
                decodedPayload = json.loads(base64.decodebytes(payloadPartBase64.encode('utf-8')))
            except BaseException as aa:
                # UnExpected Header or Payload
                return un_authorized()
            timeNow = datetime.timestamp(datetime.now())
            if timeNow > decodedPayload['Expired']:
                # Session Ended
                return un_authorized()

            try:
                user = Admins.objects.filter(email=decodedPayload["Mail"]).first()

            except:
                return un_authorized()

            request.authentication = decodedPayload
            request.authUser = user
            # Update LastSeen
            user.updateLastSeenActivity(request)

        except BaseException as a:
            print(a)
            return un_authorized()
