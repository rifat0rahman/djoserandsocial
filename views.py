from django.shortcuts import render

# Create your views here.


def register(request):
    return render(request, 'index.html')


def forget(request):
    return render(request, 'forget.html')


def reset_pass(request,uid,token):
    data = {'uid':uid,'token':token}
    return render(request,'reset.html',{'data':data})

def active_email(request,uid,token):
    data = {'uid': uid, 'token':token}
    return render(request,'active.html',{'data':data}) 

# get google,facebook auth code and state
from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view()
def redirectSocial(request, *args, **kwargs):
    code = str(request.GET['code'])
    state = str(request.GET['state'])
    json_obj = {'code': code, 'state': state}
    return JsonResponse(json_obj)

@api_view()
def redirectSocialfacebook(request, *args, **kwargs):
    code = str(request.GET['code'])
    state = str(request.GET['state'])
    json_obj = {'code': code, 'state': state}
    return JsonResponse(json_obj)

# stripe settings
from django.shortcuts import render, redirect
from django.urls import reverse
import stripe
stripe.api_key = "sk_test_51INwc9Ktmusr7YA2Pr6Z6S3xeY6IAJNnnJ792PyfhaI8yMOqP5kCLWmTDo1TCirzZOEMH0ruiiFqyRYGj8SMBXwq00J1Jqqf7X"

def stripee(request):
    
    return render (request,'stripe.html')


def charge(request):

    if request.method == 'POST':
        print('Data',request.POST)
        amount = request.POST['amount']
        customer = stripe.Customer.create(
            email = request.POST['email'],
            name = request.POST['nickname'],
            source = request.POST['stripeToken']
        )   
        charge = stripe.Charge.create(
            customer = customer,
            amount = int(amount)*100,
            currency = 'usd',
            description = 'Its for testing',
        )

    return redirect(reverse('success',args=[amount]))


def success (request,args):
    amount = args
    return render(request,'charge.html',{'amount':amount})