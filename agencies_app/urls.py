from django.urls import path
from agencies_app import views


urlpatterns = [
    path('profil/', views.myprofileAgency_view, name = "Mon profile"),
    path('ma-propriete/', views.mypropertyAgency_view, name = "Les propriétés"),
    path('nouveau-propriete/', views.newpropertyAgency_view, name = "Nouvelle propriété"),
    path('favorite-propriete/', views.bookmarkedAgency_view, name = "Propriétés favorites"),
    path('mot-de-passe/', views.changepasswordAgency_view, name = "Chnager de mot de passe"),
    path('liste-agences/', views.listagenciesAgency_view, name = "Liste des agences"),
    path('tableau-de-bord/', views.dashboardAgency_view, name =  "Tableau de bord")
]