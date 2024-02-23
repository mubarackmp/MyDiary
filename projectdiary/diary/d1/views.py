from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Diary

# Create your views here.
def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('pass1')
        password2 = request.POST.get('pass2')
        if password1 == password2:
            if User.objects.filter(username=username,email=email).exists():
                messages.info(request,'username alreadt exists!!!')
                print('user already have')
                return redirect(user_signup)
            else:
                user = User.objects.create_user(username,email,password1)
                user.save()
                print('sinup successfull')
                return redirect(user_login)
        else:
            print('wrong password')
            return redirect(user_signup)
    return render(request,'signup.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(diarye)
        else:
            messages.info(request,'user not exist')
            print('user not exist')
            return redirect(user_login)
    return render(request,'login.html')  

def user_logout(request):
    logout(request)
    return redirect(user_login)

def diarye(request):
    if request.method == 'POST':
        date=request.POST.get('datee')
        heading = request.POST.get('head')
        diary=request.POST.get('diary')
        data=Diary.objects.create(dates=date,heading=heading ,diarys=diary, user=request.user)
        data.save()
        return pages(request)
    return render(request,'demo.html')


def pages(request):
    p=Diary.objects.filter(user =request.user)
    return render(request,'pages.html',{'c':p})

def dia(request,r):
    a=Diary.objects.get(id=r)
    return render(request,'note.html',{'note':a})

def dlete(request,p):
    a=Diary.objects.get(pk=p)
    a.delete()
    return pages(request)

def editediarye(request,q):
    a=Diary.objects.get(pk=q)
    if request.method == 'POST':
        date=request.POST.get('datee')
        heading = request.POST.get('head')
        diary=request.POST.get('diary')
        a.delete()
        data=Diary.objects.create(dates=date,heading=heading ,diarys=diary, user=request.user)
        data.save()
        return pages(request)
    return render(request,'demoedit.html',{'d':a})