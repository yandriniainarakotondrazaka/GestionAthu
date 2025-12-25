from django.contrib import admin
from django.urls import path, include
from Gestioncars import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inscription', views.inscription, name= 'inscription'),
    path('', views.connexion, name='connexion'),
    path('',include('Gestioncars.urls')),
    path('acceuil/', views.acceuil, name='acceuil'),
    path('list_voiture/',views.list_voiture,name='list_voiture'),
    path('deconnexion/',views.deconnexion, name='deconnexion'),
]

