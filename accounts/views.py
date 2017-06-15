from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

# Create your views here.

def home_page(request):
    name = 'Narendra Avula'
    numbers = [1,2,3,4,5]
    args = {
        'myName' : name,
        'numbers' : numbers
    }
    return render(request, 'accounts/home.html', args)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/profile/')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/register_form.html', args)



def view_profile(request):
    args = {
        'user': request.user,
        'first_name' : request.user.first_name,
        'last_name' : request.user.last_name,
        'email' : request.user.email
    }
    return render(request, 'accounts/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else:
        form = UserChangeForm(instance=request.user)
        args = {
            'form' : form
        }
        return render(request, 'accounts/edit_profile.html', args)








# def home_page(request):
#     return HttpResponse('Home Page!')

# def home_page(request):
#     name = 'Narendra Avula'
#     numbers = [1,2,3,4,5]
#     args = {
#         'myName' : name,
#         'numbers' : numbers
#     }
#     return render(request, 'accounts/login.html', args)
