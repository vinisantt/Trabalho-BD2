from django.urls import path
from .views import home, consultaBanco, quantidadeTotal

urlpatterns = [
    path('', home,name='home'),
    path('consulta', consultaBanco, name='consultaBanco'),
    path('qt/<str:pk>', quantidadeTotal, name='quantidadeTotal'),
]
