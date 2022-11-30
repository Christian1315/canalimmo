from django.urls import path
from users_app import views


urlpatterns = [
    path('connexion/', views.login_view, name = "connexion"),
    path('inscription-user/', views.signupUser_view, name = "inscription-user"),
    path('inscription-agent/', views.signupAgent_view, name = "inscription-agent"),
    path('inscription-agence/', views.signupAgency_view, name = "inscription-agence"),
    path('deconnection/', views.logout_view, name = "déconnection"),
]