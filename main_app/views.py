from django.shortcuts import render
from restapi.views import addUser, getData
from .forms import RegisterClient, EmailVerification, LoginPage
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from urllib.parse import quote
from project.settings import EMAIL_HOST_USER
from itsdangerous import URLSafeSerializer
import random
from .models import users
# Create your views here.

def encryptdata(data):
    serializer = URLSafeSerializer("1234567890")
    encrypteddata = serializer.dumps(data)
    return encrypteddata
def decrypt_data(encrypted_data):

    serializer = URLSafeSerializer('1234567890')
    decrypted_data = serializer.loads(encrypted_data)
    return decrypted_data

def userRegistration(request):    
    context={}
    context['form'] = RegisterClient()
    if request.method == "POST":
        data=dict(request.POST)
        user = data["username"][0]
        password = data["password"][0]
        email = data["email"][0]
        # u_type=data["user_type"][0]
        addUser(request)
        # is_Ops = data["is_Ops"][0]
        encrypted_user_data=encryptdata({"username":user,"password":password,"email":email})
        subject = "Test_App Email Verification"
        code=random.randrange(1000,9999)
        verification_code = encryptdata(code)
        print(request)
        message = "Verification Code: " + str(code)    
        recepient = email
        print(send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently= False))
        encrypted = "rien"
        url = quote("/app/email-validation/"+verification_code+"/")
        return HttpResponseRedirect(url)
    return(render(request, "index.html",context))


def emailValidation(request,verification_code):
    verification_code = decrypt_data(verification_code)    
    context={}
    context["form"] = EmailVerification()
    if request.method == "POST":
        print("AFTER POSTING")
        entered_code= request.POST.get("four_digit_code")
        print(entered_code)
        print(verification_code)
        if str(entered_code) == str(verification_code):
            return HttpResponseRedirect("/app/login", getData(request))
        else:

            print("MAJOR ERROR")
    return(render(request, "email-validation.html", context))


def login(request):
    context={}
    context["form"] = LoginPage
    if request.method == "POST":
        data_dict= dict(request.POST)
        username = data_dict["username"][0]
        password = data_dict["password"][0]
        user_data = users.objects.all().values().filter(username=username)[0]
        if user_data['password'] == password:
            if user_data['is_ops']:
                print("ops user, logged in")
                return HttpResponseRedirect("/app/file-upload/")
            else:
                print("Client User Logged In")
                return HttpResponseRedirect("/app/file-download/")
        
    return(render(request,"login.html", context))


def file_upload(request):
    return render(request,"upload-files.html")

def file_download(request):
    return render(request,"download-list.html")

