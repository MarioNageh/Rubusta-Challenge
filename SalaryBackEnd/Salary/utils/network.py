def get_client_ip(request):
    ip = "Mario"
    try:
        ip = request.META['REMOTE_ADDR']
    except BaseException as s:
        ip = "Mario"
    return ip
