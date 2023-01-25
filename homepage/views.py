from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import NewsPost, HomepageBanner
from .serializers import NewsPostSerializer, HomepageBannerSerializer

class HomepageView(ListAPIView):
    queryset = HomepageBanner.objects.all()
    serializer_class = HomepageBannerSerializer
    permission_classes = (permissions.AllowAny,)

class NewsPostListView(ListAPIView):
    queryset = NewsPost.objects.order_by('-date_created')
    serializer_class = NewsPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)

class NewsPostDetailView(RetrieveAPIView):
    queryset = NewsPost.objects.order_by('-date_created')
    serializer_class = NewsPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)
        
class NewsPostFeaturedView(ListAPIView):
    queryset = NewsPost.objects.filter(featured=True)
    serializer_class = NewsPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)