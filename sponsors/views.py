from rest_framework import permissions
from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *

class SponsorsListView(ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    permission_classes = (permissions.AllowAny,)

class GokartSponsorsListView(ListAPIView):
    queryset = Sponsor.objects.filter(division='GOKART')
    serializer_class = SponsorSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)

class EVSponsorsListView(ListAPIView):
    queryset = Sponsor.objects.filter(division='EV')
    serializer_class = SponsorSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)