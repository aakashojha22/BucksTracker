
from django.views.generic import (TemplateView )
# Create your views here.
from .forms import UserInfoForm,UserForm
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout




class IndexView(TemplateView):
    template_name = 'accounts/index.html'


def signup(request):

    if request.method =='POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user=user
            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()
            return redirect('thankyou')

        else:
            print(user_form.errors,profile_form.errors)


    else:
        user_form=UserForm()
        profile_form=UserInfoForm()

    return render(request,'accounts/signup.html',{
            'user_form':user_form,
            'profile_form':profile_form,

        })

class ThankyouView(TemplateView):
    template_name = 'accounts/thankyou.html'



def user_login(request):

    if request.method== 'POST':
        username=request.POST.get('username')
        password = request.POST.get('password')

        user= authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("account not active")

        else:
            info='login failed'
            return render(request,'accounts/login.html',{'message':info})

    else:
        return render(request,'accounts/login.html',{})



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))