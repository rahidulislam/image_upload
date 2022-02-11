from unicodedata import name
import django


from django.urls import path
from core.views import HomeView,PescriptionCreateView

app_name = 'core'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('pescription_create/',PescriptionCreateView.as_view(), name='prescription-create'),
]
