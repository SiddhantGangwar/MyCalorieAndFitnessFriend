from locale import currency
from django.shortcuts import render
from MyCalorieAndFitnessFriend.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
import razorpay
# Create your views here.
client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
def pay(request):
   # DATA = {
   # "amount": 100,
    #"currency": "INR",
    #"receipt": "receipt#1",
    #"notes": {
       # "key1": "value3",
        #"key2": "value2"
    #}
    #}
    amountdonated=request.GET.get('amountdonated')
    order_amount=500
    if amountdonated is not None:
        order_amount=int(amountdonated)
    order_amountp=order_amount*100
    order_currency='INR'
    payment_order=client.order.create(dict(amount=order_amountp,currency=order_currency,payment_capture=1))
    payment_order_id=payment_order['id']
    context ={
        'amount': order_amount, 'api_key':RAZORPAY_API_KEY ,'order_id':payment_order_id
    }
    return render(request,'pay.html',context)