from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.db.models import Q


""" For user registration """

def signupUser_view(request):

    error = False
    error_message = ""

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        re_password = request.POST['re_password']
        rgdp = request.POST['rgdp']
        

        # Validation email
        try:
            validate_email(email)

        except:
            error = True
            error_message = "Veuillez entrer un e-mail valide !"

        #mot de passe vérification
        if password != re_password:
            error = True
            error_message = "Les mots de passe ne correspondent pas. Veuillez réesayer !"

        # Utilisateur existant
        user = User.objects.filter(Q(email=email)).first()
        if user:
            error = True
            error_message = f"Un ultilisateur avec l'email {email} existe déjà."

        # Création de l'user quand il n'y a pas d'erreur
        if error == False :
            user = User.objects.create_user('', email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return redirect

        print(first_name, last_name, phone, email, password, re_password, rgdp)


    data = {
        'error' : error,
        'error_message' : error_message
    }

    return render(request, 'register-customer.html')



def signupAgent_view(request):

    error = False
    error_message = ""

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']
        phone = request.POST['phone']
        type_user = request.POST['type_user']

        # Validation email
        try:
            validate_email(email)

        except:
            error = True
            error_message = "Veuillez entrer un e-mail valide !"

        #mot de passe vérification
        if password != re_password:
            error = True
            error_message = "Les mots de passe ne correspondent pas. Veuillez réesayer !"

        # Utilisateur existant
        user = User.object.filter(Q(email=email)).first()
        if user:
            error = True
            error_message = f"Un ultilisateur avec l'email {email} existe déjà."

        # Création de l'user quand il n'y a pas d'erreur
        if error == False :
            user = User.objects.create_user('', email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return redirect


    data = {
        'error' : error,
        'error_message' : error_message
    }
    return render(request, 'register-agent.html')


def signupAgency_view(request):

    error = False
    error_message = ""

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']
        phone = request.POST['phone']
        type_user = request.POST['type_user']

        # Validation email
        try:
            validate_email(email)

        except:
            error = True
            error_message = "Veuillez entrer un e-mail valide !"

        #mot de passe vérification
        if password != re_password:
            error = True
            error_message = "Les mots de passe ne correspondent pas. Veuillez réesayer !"

        # Utilisateur existant
        user = User.object.filter(Q(email=email)).first()
        if user:
            error = True
            error_message = f"Un ultilisateur avec l'email {email} existe déjà."

        # Création de l'user quand il n'y a pas d'erreur
        if error == False :
            user = User.objects.create_user('', email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return redirect


    data = {
        'error' : error,
        'error_message' : error_message
    }
    return render(request, 'register-agency.html')


""" For user login """

def login_view(request):

    if request.method == "POST":
        user_email = request.POST['user_email']
        user_password = request.POST['user_password']

        user = User.objects.filter(email= user_email).first()


""" For the disconnection of a user """

def logout_view(request):
    return