from rest_framework.permissions import IsAuthenticated

from zbook.system.views import BaseListCreateAPIView, BaseRetrieveUpdateAPIView
from .models import VoucherSubType, Voucher
from .serializers import VoucherSubTypeSerializer, VoucherSerializer


class VoucherSubTypeListCreateAPIView(BaseListCreateAPIView):
    queryset = VoucherSubType.objects.all().order_by('-id')
    serializer_class = VoucherSubTypeSerializer
    permission_classes = [IsAuthenticated]


class VoucherSubTypeRetrieveUpdateAPIView(BaseRetrieveUpdateAPIView):
    queryset = VoucherSubType.objects.all()
    serializer_class = VoucherSubTypeSerializer
    permission_classes = [IsAuthenticated]


class VoucherListCreateAPIView(BaseListCreateAPIView):
    queryset = Voucher.objects.all().order_by('-id')
    serializer_class = VoucherSerializer
    permission_classes = [IsAuthenticated]


class VoucherRetrieveUpdateAPIView(BaseRetrieveUpdateAPIView):
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer
    permission_classes = [IsAuthenticated]
