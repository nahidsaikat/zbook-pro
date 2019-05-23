from django.urls import path, include
from .views import AccountCreateView


urlpatterns = [
    path('add/', AccountCreateView.as_view(), name='account-add'),
]
