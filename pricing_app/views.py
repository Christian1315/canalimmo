from django.shortcuts import render, redirect

def pricing_view(request):
    return render(request, 'index.html')

def payment_view(request):
    return render(request, 'list-layout-with-sidebar.html')


def userrule_view(request):
    return render(request, 'list-layout-with-sidebar.html')
