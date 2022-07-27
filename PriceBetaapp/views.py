from email.message import EmailMessage
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.http import HttpResponse, request
from django.contrib import messages
from PriceBetaproject import settings
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from . tokens import generate_token


# Create your views here.

#   @login_required(login_url='PriceBetaapp/signin.html')#test for differences in users
def index(request):
	return render(request, "index.html")

def signup(request):

    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        password2 = request.POST['password2']

       


def signin(request):
    
    if request.method == 'POST':
        email = request.POST('email')
        password = request.POST('password')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Information provided')
            return redirect('signin.html')

    else:
        return render(request, 'signin.html')


@login_required(login_url='signin.html')#test for differences in users
def signout(request):
    auth.logout(request)
    return redirect('index.html')


