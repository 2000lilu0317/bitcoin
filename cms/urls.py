from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve 

from . import views

app_name = 'cms'

urlpatterns = [
    path('bitcoin/', views.BitcoinView.as_view(), name='bitcoin'),
    path('ethereum/', views.EthereumView.as_view(), name='ethereum'),
    path('', views.AboutView.as_view(), name='about'),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]