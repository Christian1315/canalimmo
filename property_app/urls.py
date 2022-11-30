from django.urls import path
from property_app import views


urlpatterns = [
    path('publier-une-propriete/', views.addProperty_view, name = "Publier une propriété"),
    path('modifier-une-propriete/', views.modifyProperty_view, name = "Modifier une propriété"),
    path('supprimer-une-propriete/', views.deleteProperty_view, name = "Supprimer une propriété"),
    path('voir-une-propriete/', views.viewProperty_view, name = "Voir une propriété"),
    path('favorite-propriete/', views.bookmarkProperty_view, name = "Propriété favorite"),
    path('detail-propriete/', views.detailProperty_view, name = "Détails des propriété")
]