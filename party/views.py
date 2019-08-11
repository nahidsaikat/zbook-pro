from rest_framework.permissions import IsAuthenticated

from system.views import BaseListCreateAPIView
from .models import PartySubType
from .serializers import PartySubTypeSerializer


class PartySubTypeListCreateAPIView(BaseListCreateAPIView):
    queryset = PartySubType.objects.all().order_by('-id')
    serializer_class = PartySubTypeSerializer
    permission_classes = [IsAuthenticated]
