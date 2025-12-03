from django.shortcuts import render


def base(request):
    return render(request, 'base.html')


def cart(request):
    return render(request, 'cart.html')