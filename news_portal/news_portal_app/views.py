from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, logout
from news_portal_app.models import *
from news_portal_app.forms import *

# Create your views here.
def Registration_page(request):
    if request.method== 'POST':
        form_data=RegistrationForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('Login_page')

    form_data=RegistrationForm()
    context={
        'form_data':form_data,
        'form_title': 'Resister Form',
        'form_btn': 'Register'
    }
    return render(request, 'master/base-form.html',context)

def Login_page(request):
    if request.method=='POST':
        form_data=LoginForm(request, request.POST)
        if form_data.is_valid():
            user=form_data.get_user()
            if user:
                login(request, user)
                return redirect('home')

    form_data=LoginForm()

    context={
            'form_data':form_data,
            'form_title': 'Login Form',
            'form_btn': 'Login'
        }
    return render(request, 'master/base-form.html',context)


def logout_page(request):
    logout(request)
    return redirect('Login_page')



def home(request):
    return render(request, 'home.html')

def newsList(request):
    news_data=newsModel.objects.all()

    context={
        'news_data':news_data
    }
    return render(request, 'newsList.html',context)

def addNews(request):
    if request.method == 'POST':
        form_data = newsForm(request.POST, request.FILES)

        if form_data.is_valid():
            form_data.save()
            return redirect('newsList')
    else:
        form_data = newsForm()

    context = {
        'form_data': form_data,
        'form_title': 'Add news form',
        'form_btn': 'Add news'
    }

    return render(request, 'master/base-form.html', context)

def editNews(request, id):
    news_data=newsModel.objects.get(id=id)
    if request.method == 'POST':
        form_data = newsForm(request.POST, request.FILES, instance=news_data)

        if form_data.is_valid():
            form_data.save()
            return redirect('newsList')
    else:
        form_data = newsForm(instance=news_data)

    context = {
        'form_data': form_data,
        'form_title': 'update news form',
        'form_btn': 'update news'
    }

    return render(request, 'master/base-form.html', context)


def deletenews(request,id):
    news_data=newsModel.objects.get(id=id)
    news_data.delete()

    return redirect('newsList')