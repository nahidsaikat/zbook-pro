from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import AccountSubTypeSerializer, AccountSerializer
from .models import AccountSubType, Account


class AccountSubTypeListCreateAPIView(ListCreateAPIView):
    queryset = AccountSubType.objects.all().order_by('-id')
    serializer_class = AccountSubTypeSerializer
    permission_classes = [IsAuthenticated]


class AccountSubTypeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = AccountSubType.objects.all()
    serializer_class = AccountSubTypeSerializer
    permission_classes = [IsAuthenticated]


class AccountListCreateAPIView(ListCreateAPIView):
    queryset = Account.objects.all().order_by('-id')
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]


class AccountRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]
