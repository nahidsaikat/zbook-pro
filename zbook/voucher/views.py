from rest_framework.permissions import IsAuthenticated

from zbook.system.views import BaseListCreateAPIView, BaseRetrieveUpdateAPIView
from .models import VoucherSubType
from .serializers import VoucherSubTypeSerializer


class VoucherSubTypeListCreateAPIView(BaseListCreateAPIView):
    queryset = VoucherSubType.objects.all().order_by('-id')
    serializer_class = VoucherSubTypeSerializer
    permission_classes = [IsAuthenticated]


class VoucherSubTypeRetrieveUpdateAPIView(BaseRetrieveUpdateAPIView):
    queryset = VoucherSubType.objects.all()
    serializer_class = VoucherSubTypeSerializer
    permission_classes = [IsAuthenticated]
