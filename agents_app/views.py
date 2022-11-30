from django.shortcuts import render

def myprofileAgent_view(request):
    return render(request, 'my-profil.html')

def mypropertyAgent_view(request):
    return render(request, 'my-property.html')

def newpropertyAgent_view(request):
    return render(request, 'submit-property-dashboard.html')

def bookmarkedAgent_view(request):
    return render(request, 'bookmark-list.html')

def changepasswordAgent_view(request):
    return render(request, 'change-password.html')

def listagentsAgent_view(request):
    return render(request, 'agents.html')

def dashboardAgent_view(request):
    return render(request, 'dashboard.html')

def publicAgent_view(request):
    return render(request, 'agent-page.html')


#======= CHRISTIAN ========# 

def addAgent(request):
    pass