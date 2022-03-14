from django.urls import path

from . import views

app_name = 'cms'

urlpatterns = [
    path('bitcoin/', views.BitcoinView.as_view(), name='bitcoin'),
    path('ethereum/', views.EthereumView.as_view(), name='ethereum'),
    path('', views.AboutView.as_view(), name='about'),
]