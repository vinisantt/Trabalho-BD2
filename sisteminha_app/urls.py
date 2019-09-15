from django.urls import path
from .views import home, consultaBanco

urlpatterns = [
    path('', home,name='home'),
    path('consulta', consultaBanco, name='consultaBanco'),
]
