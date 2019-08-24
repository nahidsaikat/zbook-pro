from django.urls import path, include
from .views import VoucherSubTypeListCreateAPIView, VoucherSubTypeRetrieveUpdateAPIView, VoucherListCreateAPIView, \
    VoucherRetrieveUpdateAPIView


subtype_urlpatterns = [
    path('', VoucherSubTypeListCreateAPIView.as_view(), name='list-create'),
    path('<int:pk>/', VoucherSubTypeRetrieveUpdateAPIView.as_view(), name='detail-update'),
]

urlpatterns = [
    path('subtype/', include((subtype_urlpatterns, 'subtype'))),

    path('', VoucherListCreateAPIView.as_view(), name='list-create'),
    path('<int:pk>/', VoucherRetrieveUpdateAPIView.as_view(), name='detail-update'),
]
