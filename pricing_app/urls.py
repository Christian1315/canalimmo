from django.urls import path
from pricing_app import views


urlpatterns = [
    path('nos-packs/', views.pricing_view, name = "Nos Packs"),
    path('paiement/', views.payment_view, name = "Paiement"),
    path('role-utilisateur/', views.userrule_view, name = "Rôle"),
]