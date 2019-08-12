from rest_framework.permissions import IsAuthenticated

from zbook.system.views import BaseListCreateAPIView, BaseRetrieveUpdateAPIView
from .models import PartySubType, Customer, Vendor
from .serializers import PartySubTypeSerializer, CustomerSerializer, VendorSerializer


class PartySubTypeListCreateAPIView(BaseListCreateAPIView):
    queryset = PartySubType.objects.all().order_by('-id')
    serializer_class = PartySubTypeSerializer
    permission_classes = [IsAuthenticated]


class PartySubTypeRetrieveUpdateAPIView(BaseRetrieveUpdateAPIView):
    queryset = PartySubType.objects.all()
    serializer_class = PartySubTypeSerializer
    permission_classes = [IsAuthenticated]


class CustomerListCreateAPIView(BaseListCreateAPIView):
    queryset = Customer.objects.all().order_by('-id')
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


class CustomerRetrieveUpdateAPIView(BaseRetrieveUpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


class VendorListCreateAPIView(BaseListCreateAPIView):
    queryset = Vendor.objects.all().order_by('-id')
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]


class VendorRetrieveUpdateAPIView(BaseRetrieveUpdateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]
