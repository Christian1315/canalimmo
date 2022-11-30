from django.shortcuts import render, redirect

def addProperty_view(request):
    return render(request, 'submit-property.html')

def modifyProperty_view(request):
    return render(request, 'list-layout-with-sidebar.html')


def deleteProperty_view(request):
    return render(request, 'list-layout-with-sidebar.html')


def viewProperty_view(request):
    return render(request, 'agents.html')

def bookmarkProperty_view(request):
    return render(request, 'agents.html')

def detailProperty_view(request):
    return render(request, 'single-property-3.html')