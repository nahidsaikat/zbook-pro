from django.urls import path, include
from .views import PartySubTypeListCreateAPIView


subtype_urlpatterns = [
    path('', PartySubTypeListCreateAPIView.as_view(), name='list-create'),
]

urlpatterns = [
    path('subtype/', include((subtype_urlpatterns, 'subtype'))),
]
