from django.shortcuts import render, HttpResponse

# Create your views here.

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


def home_page(request):
    name = 'Narendra Avula'
    numbers = [1,2,3,4,5]
    args = {
        'myName' : name,
        'numbers' : numbers
    }
    return render(request, 'accounts/home.html', args)