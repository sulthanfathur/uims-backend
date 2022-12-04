from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import NewsPost
from .serializers import NewsPostSerializer

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