from unicodedata import category
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import NewsPost, TeamMember, TeamRole
from .serializers import NewsPostSerializer, TeamMemberSerializer

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

class TeamMemberListView(ListAPIView):
    # queryset = TeamMember.objects.all()
    # serializer_class = TeamMemberSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        members = TeamMember.objects.all()
        team_member_serializer = TeamMemberSerializer(
            members, many=True)
        response = {
            "status": 200,
            "message": "success",
            "members": team_member_serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)
