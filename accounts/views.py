from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrationForm

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
            return redirect('/account')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/register_form.html', args)














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
