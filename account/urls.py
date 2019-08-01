from django.urls import path, include
from .views import AccountSubTypeListCreateAPIView, AccountSubTypeRetrieveUpdateAPIView, AccountListCreateAPIView, \
    AccountRetrieveUpdateAPIView


subtype_urlpatterns = [
    path('', AccountSubTypeListCreateAPIView.as_view(), name='list-create'),
    path('<int:pk>/', AccountSubTypeRetrieveUpdateAPIView.as_view(), name='detail-update'),
]

urlpatterns = [
    path('subtype/', include((subtype_urlpatterns, 'subtype'))),

    path('', AccountListCreateAPIView.as_view(), name='list-create'),
    path('<int:pk>/', AccountRetrieveUpdateAPIView.as_view(), name='detail-update'),
]
