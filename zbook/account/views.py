from rest_framework.permissions import IsAuthenticated

from zbook.system.views import BaseListCreateAPIView, BaseRetrieveUpdateAPIView
from .serializers import AccountSubTypeSerializer, AccountSerializer
from .models import AccountSubType, Account


class AccountSubTypeListCreateAPIView(BaseListCreateAPIView):
    queryset = AccountSubType.objects.all().order_by('-id')
    serializer_class = AccountSubTypeSerializer
    permission_classes = [IsAuthenticated]


class AccountSubTypeRetrieveUpdateAPIView(BaseRetrieveUpdateAPIView):
    queryset = AccountSubType.objects.all()
    serializer_class = AccountSubTypeSerializer
    permission_classes = [IsAuthenticated]


class AccountListCreateAPIView(BaseListCreateAPIView):
    queryset = Account.objects.all().order_by('-id')
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]


class AccountRetrieveUpdateAPIView(BaseRetrieveUpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]
