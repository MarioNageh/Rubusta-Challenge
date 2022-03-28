from datetime import datetime, timedelta
import hashlib
import hmac
import base64

import json
import hashlib

from SalaryBackEnd.settings import TIME_OF_RE_SYNC, SECRET_KEY_AUTH


def generateAuthToken(user):
    # The Token Contain (header.payload.signature)
    header = json.dumps({"SignedBy": "Mario"})
    nextReSyncTime = datetime.today() + timedelta(seconds=TIME_OF_RE_SYNC)

    payload = json.dumps({
        "IdAdmin": user.idAdmin,
        "UserName": f'{user.firstName} {user.lastName}',
        "FirstName": user.firstName,
        "LastName": user.lastName,
        "Mail": user.email,
        "Expired": datetime.timestamp(nextReSyncTime),
    })
    headerBase64 = base64OfString(header)
    payloadBase64 = base64OfString(payload)
    data = f'{headerBase64.decode("utf-8")}.{payloadBase64.decode("utf-8")}'
    signature = hmac.new(SECRET_KEY_AUTH.encode('utf-8'), data.encode('utf-8'), hashlib.sha256).hexdigest()
    return f'{data}.{signature}'


def base64OfString(data):
    return base64.b64encode(data.encode('utf-8'))


def base64ToByte(data):
    return base64.decodebytes(data.encode('utf-8'))


def hashSha1(txt):
    return hashlib.sha1(txt.encode()).hexdigest()
