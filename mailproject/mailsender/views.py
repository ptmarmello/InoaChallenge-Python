from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def mailsender(message="Sorry, but something went wrong. Please contact your administrator."):
    send_mail('Assunto', message ,'towho', ['towho1','towho2'])

    return HttpResponse('Oh Hello, Peter')