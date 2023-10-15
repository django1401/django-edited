from django.shortcuts import render,redirect
from .forms import CustomUserCreation
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomeUser, Profile
from .forms import CaptchaForm, AuthenticationForm, CustomUserProfile




def Login(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'GET':
        form = AuthenticationForm()
        captcha = CaptchaForm()
        return render(request,'registration/login.html', context={'form': form,'captcha': captcha})
    elif request.method == 'POST':
        captcha_form = CaptchaForm(request.POST)
        if captcha_form.is_valid():
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')      
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, 'Invalid email or password')
                return redirect(request.path_info)
        else:
            messages.add_message(request, messages.ERROR, 'Invalid captcha')
            return redirect(request.path_info)


@login_required
def Logout(request):
    logout(request)
    return redirect('/')


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'GET':
        captcha = CaptchaForm()
        form = CustomUserCreation()
        return render(request,'registration/signup.html', context={'form': form,'captcha': captcha})
    else:
        captcha_form = CaptchaForm(request.POST)
        if captcha_form.is_valid():
            form = CustomUserCreation(request.POST)
            if form.is_valid():
                form.save()
                email = request.POST.get('email')
                password = request.POST.get('password1')
                user=authenticate(email=email,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('accounts:complate_profile')
                else:
                    messages.add_message(request, messages.ERROR, 'Invalid email or password')
                    return redirect(request.path_info)
            else:
                messages.add_message(request, messages.ERROR, 'Invalid email or password')
                return redirect(request.path_info)
            
        else:
            messages.add_message(request, messages.ERROR, 'Invalid captcha')
            return redirect(request.path_info)
        
def complate_profile(request):
    if request.method == 'GET':
        #form = CustomUserProfile()
        return render(request,'registration/profile.html')
    elif request.method == 'POST':
        user = Profile.objects.get(user=request.user)
        print (user, request.POST, request.FILES, sep='\n')
        form = CustomUserProfile(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('/')

        


# Create your views here.
