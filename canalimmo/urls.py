"""canalimmo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from canalimmo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name = "accueil"),
    path('contact/', views.contact_view, name = "contact"),
    path('a-louer/', views.listForRent_view, name = "a_louer"),
    path('a-vendre/', views.listForSale_view, name = "a_vendre"),
    path('filtre/', views.filerProperty_view, name = "filtre"),

    #=======CHRISTIAN ==========#
    path('a-propos/',views.about_page_view,name='about_page'),
    path('contact/',views.contact_page_view,name='contact_page'),
    path('partenaire/',views.partenanire_page_view,name='partenanire_page'),
    path('donner-un-avis/',views.donner_un_avis_page_view,name='donner_un_avis_page'),
    path('mon-profil/',views.mon_profil_page_view,name='donner_un_avis_page'),
    path('mes-favorites/',views.mes_favorites_page_view,name='mes_favorites_page'),
    path('devenir-agent/',views.devenir_agent_page_view,name='devenir_agent'),
    path('devenir-agence/',views.devenir_agent_page_view,name='devenir_agent'),
    path('avertissements/',views.avertissements_page_view,name='avertissements_page'),


    #======= END ==========#

    path('', include('agencies_app.urls')),
    path('', include('agents_app.urls')),
    path('', include('pricing_app.urls')),
    path('', include('property_app.urls')),
    path('', include('users_app.urls')),
    path('', include('blog_app.urls')),
]