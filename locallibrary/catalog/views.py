from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
# import smtplib, os


# Create your views here.


def index(request):
    try:
        send_mail('Test Mail', 'Welcome to my Django Project', 'akshaykumardjangotest@gmail.com', ['akshayg2697@gmail.com',], fail_silently=False,)
    except:
        return HttpResponse("Mail has been sent")

    # return render(request,'sent.html')



# 'mohangokulcse@gmail.com '