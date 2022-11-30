from django.shortcuts import render

def myprofileAgency_view(request):
    return render(request, 'my-profil.html')

def mypropertyAgency_view(request):
    return render(request, 'my-property.html')

def newpropertyAgency_view(request):
    return render(request, 'submit-property-dashboard.html')

def bookmarkedAgency_view(request):
    return render(request, 'bookmark-list.html')

def changepasswordAgency_view(request):
    return render(request, 'change-password.html')

def listagenciesAgency_view(request):
    return render(request, 'agencies.html')

def dashboardAgency_view(request):
    return render(request, 'dashboard.html')