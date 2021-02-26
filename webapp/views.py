from django.shortcuts import render
from .forms import GstForm
from .models import *
from django.http import HttpResponse
import math, random
from twilio.rest import Client
# Create your views here.

def index(request):
    return render(request,'index.html',{})

def verify_otp(request):
    if request.method == 'POST':
        otpFromInput = request.POST.get("otp_verify")
        OtpDataFromDb = Otp.objects.last()
        OtpFromDb = getattr(OtpDataFromDb, "otp")
        if int(otpFromInput) == int(OtpFromDb):
            return HttpResponse('True')
        else:
            return HttpResponse('False')

def send_otp(request):
    if request.method == 'POST':
        otp = generateOTP()
        number = request.POST.get("phone_number")
        account_sid = 'ACaf25aa65a3f02f3e9ee729c0a1db1e88'
        auth_token = 'dbb9f82a54d7131ee8470d53408f1918'
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body="Hello, Sir your OTP for login is {}".format(otp),
                            from_='+17792073322',
                            to='+91{}'.format(number)
                        )
        
        print(message.sid)
        
        otpData = Otp()
        otpData.user_id = number
        otpData.otp = otp
        otpData.save()

        return HttpResponse("OTP sent")

def generateOTP() : 
    digits = "0123456789"
    OTP = "" 
    for i in range(4) : 
        OTP += digits[int(math.floor(random.random() * 10))] 
    return OTP 

def register(request):
    form = GstForm()
    if request.method == 'POST':
        form=GstForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse("Successfully saved the data to the database")
    else:
        return render(request,'register.html',{'form':form})

def services(request):
    return render(request,'services.html',{})

def portfolio(request):
    return render(request,'portfolio.html',{})

def blog(request):
    return render(request,'blog.html',{})

def contactus(request):
    return render(request,'contact-us.html',{})

def projectItem(request):
    return render(request,'project-item.html',{})

def blogItem(request):
    return render(request,'blog-item.html',{})

def noPageFound(request):
    return render(request,'404.html',{})