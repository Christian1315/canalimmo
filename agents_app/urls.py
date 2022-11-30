from django.urls import path
from agents_app import views


urlpatterns = [
    path('profil/', views.myprofileAgent_view, name = "Mon profile"),
    path('ma-propriete/', views.mypropertyAgent_view, name = "Les propriétés"),
    path('nouveau-propriete/', views.newpropertyAgent_view, name = "Nouvelle propriété"),
    path('favorite-propriete/', views.bookmarkedAgent_view, name = "Propriétés favorites"),
    path('mot-de-passe/', views.changepasswordAgent_view, name = "Chnager de mot de passe"),
    path('liste-agents/', views.listagentsAgent_view, name = "Liste des agences"),
    path('tableau-de-bord/', views.dashboardAgent_view, name =  "Tableau de bord"),
    path('agent/', views.publicAgent_view, name = "agent_profil")
]