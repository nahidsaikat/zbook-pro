from django.urls import path, include
from .views import PartySubTypeListCreateAPIView, PartySubTypeRetrieveUpdateAPIView


subtype_urlpatterns = [
    path('', PartySubTypeListCreateAPIView.as_view(), name='list-create'),
    path('<int:pk>/', PartySubTypeRetrieveUpdateAPIView.as_view(), name='detail-update'),
]

urlpatterns = [
    path('subtype/', include((subtype_urlpatterns, 'subtype'))),
]
