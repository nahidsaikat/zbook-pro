from django.urls import path, include
from .views import PartySubTypeListCreateAPIView, PartySubTypeRetrieveUpdateAPIView, CustomerListCreateAPIView


subtype_urlpatterns = [
    path('', PartySubTypeListCreateAPIView.as_view(), name='list-create'),
    path('<int:pk>/', PartySubTypeRetrieveUpdateAPIView.as_view(), name='detail-update'),
]

customer_urlpatterns = [
    path('', CustomerListCreateAPIView.as_view(), name='list-create'),
]

urlpatterns = [
    path('subtype/', include((subtype_urlpatterns, 'subtype'))),
    path('customer/', include((customer_urlpatterns, 'customer'))),
]
