from django.urls import path, include
from .views import AccountSubTypeListCreateAPIView


subtype_urlpatterns = [
    path('', AccountSubTypeListCreateAPIView.as_view(), name='list-create'),
]

urlpatterns = [
    path('subtype/', include((subtype_urlpatterns, 'subtype'))),
]
