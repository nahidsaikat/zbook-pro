from django.urls import path, include
from .views import VoucherSubTypeListCreateAPIView


subtype_urlpatterns = [
    path('', VoucherSubTypeListCreateAPIView.as_view(), name='list-create'),
    path('<int:pk>/', VoucherSubTypeListCreateAPIView.as_view(), name='detail-update'),
]

urlpatterns = [
    path('subtype/', include((subtype_urlpatterns, 'subtype'))),
]
