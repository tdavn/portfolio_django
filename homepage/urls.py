from django.urls import path
from .views import HompageView

app_name = 'homepage'

urlpatterns = [
    path('', HompageView.as_view(), name='home_id'),
]
