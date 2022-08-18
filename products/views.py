from usersmodel.models import Userperson
from products.models import Trackings
from django.shortcuts import redirect
from django.http import HttpResponse
from settings.models import Settings
from extensions.sms import send_sms
from extensions.darsad import darsad
from .models import Orders,Carts
import requests
import json
import datetime


MERCHANT = f'92fbb122-2393-4b29-937c-06af7b8c7659'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
#amount = 11000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = f'5555'  # Optional
mobile = f'miras@gmail.com'  # Optional
# Important: need to edit for realy server.
CallbackURL = f'http://127.0.0.1:8000/products/payment/verify/' #ALLOWED_HOSTS[0]


global amount

def send_request(request):
    if request.user.is_authenticated:
        orders = [order.price * order.count for order in Orders.objects.filter(cart__customer_id=request.user.id,payment_status=False).all()]
        if len(orders) >= 1 and sum(orders) > 0:
            amount = f'{sum(orders)}0'
            req_data = {
                "merchant_id": MERCHANT,
                "amount": amount,
                "callback_url": CallbackURL,
                "description": description,
                "metadata": {"mobile": mobile, "email": email}
            }
            req_header = {"accept": "application/json","content-type": "application/json'"}
            req = requests.post(url=ZP_API_REQUEST, data=json.dumps(req_data), headers=req_header)
            authority = req.json()['data']['authority']
            if len(req.json()['errors']) == 0:
                return redirect(ZP_API_STARTPAY.format(authority=authority))
            else:
                e_code = req.json()['errors']['code']
                e_message = req.json()['errors']['message']
                return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
        else:
            return redirect('/')
    else:
        return redirect('/')



def verify(request):
    t_status = request.GET.get('Status')
    t_authority = request.GET['Authority']
    if request.GET.get('Status') == 'OK':
        req_header = {"accept": "application/json","content-type": "application/json'"}
        req_data = {
            "merchant_id": MERCHANT,
            "amount": amount,
            "authority": t_authority
        }
        req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
        if len(req.json()['errors']) == 0:
            t_status = req.json()['data']['code']
            if t_status == 100:
                settings = Settings.objects.first()
                user = Userperson.objects.filter(id=request.user.id).first()
                amount = [order.price * order.count for order in Orders.objects.filter(cart__customer_id=request.user.id, payment_status=False).all()]
                cart = Carts.objects.filter(customer_id=request.user.id, payment_status=False).first()
                ref_id = str(req.json()['data']['ref_id'])
                for order in Orders.objects.filter(cart__customer_id=request.user.id, payment_status=False).all():
                    order.product.inventory -= order.count
                    order.product.save()
                    order.payment_status = True
                    order.tracking_code = ref_id
                    order.payment_date = datetime.datetime.now()
                    order.save()

                cart.payment_status = True
                cart.payment_date = datetime.datetime.now()
                cart.save()
                user.wallet += int(darsad(sum(amount), settings.paymentـpercentage))
                user.save()

                ref_id = str(req.json()['data']['ref_id'])
                product_tracking = Trackings.objects.create(cart_id=cart.id, code=f"{ref_id}",status="درحال پردازش")
                text = f"سفارش شما با موفقیت ثبت شد\n\nکد پیگیری : {ref_id}"
                send_sms(phone=user.phone, text=text)
                return HttpResponse('پرداخت با موفقیت انجام شد')
            elif t_status == 101:
                return HttpResponse('Transaction submitted : ' + str(req.json()['data']['message']))
            else:
                return HttpResponse('Transaction failed.\nStatus: ' + str(req.json()['data']['message']))
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
    else:
        return HttpResponse('Transaction failed or canceled by user')







