from settings.models import Settings
from .melipayamak import Api


def send_sms(phone,text):
    settings = Settings.objects.first()
    username = settings.sms_username
    password = settings.sms_password
    api = Api(username,password)
    sms = api.sms()
    to = f'{phone}'
    _from = settings.sms_phone
    text = f'{text}'
    response = sms.send(to,_from,text)
    return "OK"