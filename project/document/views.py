from django.shortcuts import render, redirect
from django.http import HttpRequest
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import User, Department, Document
# Create your views here.

def loginPage(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('menu')
        else:
            return redirect('login')

    return render(request, 'login.html')

def signout(request: HttpRequest):
    logout(request)
    return redirect('login')

@user_passes_test(lambda u: u.is_staff, login_url='signUp')
def signUp(request: HttpRequest):
    return render(request, 'signUp.html')

def register(request: HttpRequest):
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    email = request.POST['email']
    phone = request.POST['phone']
    username = request.POST['username']
    password = request.POST['password']
    repassword = request.POST['repassword']
    position = request.POST['position']
    
    if '' in [firstName, lastName, email, phone, username, password, repassword, position]:
        return redirect('/signUp')
    
    if password == repassword:
        user = User(
            first_name = firstName,
            last_name = lastName,
            email = email,
            phone = phone,
            username = username,
            password = password,
            position = position
        )
        user.save()
        return redirect('/')
    else:
        return redirect('/signUp')

def forgetPassword(request: HttpRequest):
    return render(request, 'forget-password.html')

def fillEmail(request: HttpRequest):
    filled_email = request.POST['email']
    
    if filled_email:
        if User.objects.filter(email=filled_email).exists():
            return render(request, 're-password.html', context={"filled_email": filled_email})
    return redirect('/forgetPassword')

def otpPassword(request: HttpRequest):
    return render(request, 'otp-password.html')

def rePassword(request: HttpRequest):
    new_password = request.GET['new_password']
    confirm_password = request.GET['confirm_password']

    if new_password == confirm_password:
        filled_email = request.GET['filled_email']
        user = User.objects.get(email=filled_email)
        
        user.set_password(new_password)
        user.save()
        
        return redirect('/')
    else:
        return redirect('/rePassword')

@login_required(login_url="menu")
def menu(request: HttpRequest):
    return render(request, 'menu.html')

def _send_receive(request, template_name, received):
    if request.method == 'POST':
        if 'cancel' in request.POST:  
            return redirect('menu')
        document = Document(
            received=received,
            sender=Department.objects.get(departmentName=request.POST['sender']),
            recipient=Department.objects.get(departmentName=request.POST['recipient']),
            date=datetime(
                year=int(request.POST['dt_year']),
                month=int(request.POST['dt_month']),
                day=int(request.POST['dt_day'])
            ),
            documentID=request.POST['documentID'],
            subject=request.POST['subject'],
            fileDocument=request.FILES['fileDocument'].read(),
            annotation=request.POST['annotation'],
            status=request.POST['status'],
            type=request.POST['type']
        )
        document.save()
        return redirect('search')
    else:
        document = Document()

    context = {'document': document}
    return render(request, template_name, context)

def receive(request: HttpRequest):
    return _send_receive(request, 'receive.html', True)

def send(request: HttpRequest):
    return _send_receive(request, 'send.html', False)

def search(request):
    query = request.GET.get('q')
    documents = Document.objects.all()
    return render(request, 'search.html', {'documents': documents})

def viewDoc(request: HttpRequest):
    return render(request, 'viewDoc.html')

