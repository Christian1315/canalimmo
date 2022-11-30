from django.shortcuts import render, redirect

def home_view(request):
    return render(request, 'index.html')

def listForRent_view(request):
    return render(request, 'list-layout-with-sidebar.html')


def listForSale_view(request):
    return render(request, 'list-layout-with-sidebar.html')


def agent_view(request):
    return render(request, 'agents.html')


def agency_view(request):
    return render(request, 'agencies.html')


def addproperty_view(request):
    return render(request, 'submit-property.html')


def login_view(request):
    return render(request, 'index.html')


def singup_view(request):
    return render(request, 'index.html')


def profil_view(request):
    return render(request, 'my-profile.html')


def contact_view(request):
    return render(request, 'contact.html')

def listForRent_view(request):
    return render(request, 'list-layout-with-sidebar.html')

def listForSale_view(request):
    return render(request, 'list-layout-with-sidebar.html')


def filerProperty_view(request):

    if request.method == 'POST':
        search_object = request.POST['search_object']
    print(search_object)
    return redirect ('/')



#======== CHRISTIAN =========#
def about_page_view(request):
    return render(request,'about-us.html')

def contact_page_view(request):
    return render(request,'contact.html')

def partenanire_page_view(request):
    return render(request,'partenaire.html')

def donner_un_avis_page_view(request):
    return render(request,'donner-un-avis.html')

def mon_profil_page_view(request):
    return render(request,'my-profile.html')

def mes_favorites_page_view(request):
    return render(request,'mes-favorites.html')

def devenir_agent_page_view(request):
    return render(request,'devenir-agent.html')

def devenir_agent_page_view(request):
    return render(request,'devenir-agence.html')

def avertissements_page_view(request):
    return render(request,'avertissements.html')