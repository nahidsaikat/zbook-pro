from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import AccountSubTypeSerializer
from .models import AccountSubType


class AccountSubTypeListCreateAPIView(ListCreateAPIView):
    queryset = AccountSubType.objects.all().order_by('id')
    serializer_class = AccountSubTypeSerializer
    permission_classes = [IsAuthenticated]
