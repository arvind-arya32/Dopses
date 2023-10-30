from django.shortcuts import render,HttpResponseRedirect
from .forms import RegisterForm ,LoginForm,Changepassword,UpdateUserForm,UpdateProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login ,logout as auth_logout,update_session_auth_hash
# Create your views here.

#Registratin form
def register(request):
    if request.method == 'POST':

     user_form = RegisterForm(request.POST)
     

     if user_form.is_valid():
        user_form.save()

        messages.success(request, 'your account created successfully')
        
        return HttpResponseRedirect('/login/')
    else:
        user_form = RegisterForm()
    return render(request,'users/register.html',{'form':user_form})




#Login Form
def login(request):

    if not request.user.is_authenticated:

        if request.method == 'POST':

            user_form = LoginForm(request=request, data=request.POST)

            if user_form.is_valid():

                uname = user_form.cleaned_data['username']
                upass = user_form.cleaned_data['password']
            

                user = authenticate(username=uname,password=upass)
                if user is not None:
                    auth_login(request, user)

                    return HttpResponseRedirect('/profile/')
        else:
        
            user_form = LoginForm()
        return render(request,'users/login.html',{'form':user_form})
    else:
        return HttpResponseRedirect('/home/')

   #FOR PROFILE PAGE VIEW FUNCTION   

def profile(request):

    if request.user.is_authenticated:

        if request.method=='POST':
            print('this post')

            user_form = UpdateUserForm(request.POST,instance=request.user)
            profile_form=UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

            if user_form.is_valid() and profile_form.is_valid():
                print('user is valid ')
                user_form.save()
                profile_form.save()
                print('Profile is saved ')
                messages.success(request,'Your Profile Updated !!')
            else:
                print('User form errors:', profile_form.errors)
                     
        else:
            user_form=UpdateUserForm(instance=request.user)
            profile_form=UpdateProfileForm(instance=request.user.profile)

        return render(request,'users/profile.html',{'name': request.user,'form':user_form,'profile_form':profile_form})
    else:
        return HttpResponseRedirect('/login/')    

 

# def home(request):
#     return render(request,'users/base.html')

def home(request):

    if request.user.is_authenticated:
     return render(request,'index.html',{'name':request.user})
    else:

     return HttpResponseRedirect('/login/') 



def manage_proposal(request):
    if request.user.is_authenticated:
        return render(request,'manage_proposals.html')

    else:
        return HttpResponseRedirect('/login/')
def contact(request):
    return render(request,'contact.html')

def guidelines(request):
    if request.user.is_authenticated:
        return render(request,'guidelines.html')

    else:
        return HttpResponseRedirect('/login/')


#LOGOUT USER    
def logout(request):

    auth_logout(request)
    return render(request,'users/logout.html')

    

#to Change password using old password
def change_password(request):

    if request.method =='POST':

        user_form = Changepassword(user=request.user, data=request.POST)

        if user_form.is_valid():

            user_form.save()
            print('save')
            messages.success(request,'your password has been changed')
            #use to update_session_auth_hash to update auth sessions data
            update_session_auth_hash(request, user_form.user)

        return HttpResponseRedirect('/profile/')
    else:
      user_form = Changepassword(user = request.user)

    return render(request,'users/change_password.html',{'form':user_form})  