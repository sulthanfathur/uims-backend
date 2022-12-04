from django.http import response
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import TeamMember
from .serializers import TeamMemberSerializer

class TeamListView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        team_principal = TeamMember.objects.filter(jabatan="TEAM_PRINCIPAL")
        team_principal_serializer = TeamMemberSerializer(team_principal, many=True)
        others = TeamMember.objects.filter(division="OTHERS").exclude(jabatan="TEAM_PRINCIPAL")
        others_serializer = TeamMemberSerializer(
            others, many=True)
        response = {
            "status": 200,
            "message": "success",
            "team_principal": team_principal_serializer.data,
            "others": others_serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)

class GokartListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)

class EVListView(ListAPIView):
    queryset = TeamMember.objects.filter(division="EV")
    serializer_class = TeamMemberSerializer
    permission_classes = (permissions.AllowAny,)

class MarketingListView(ListAPIView):
    queryset = TeamMember.objects.filter(division="MARKETING")
    serializer_class = TeamMemberSerializer
    permission_classes = (permissions.AllowAny,)

    # def get(self, request):
    #     members = TeamMember.objects.all()
    #     team_member_serializer = TeamMemberSerializer(
    #         members, many=True)
    #     response = {
    #         "status": 200,
    #         "message": "success",
    #         "members": team_member_serializer.data,
    #     }
    #     return Response(response, status=status.HTTP_200_OK)

# class NewsPostFeaturedView(ListAPIView):
#     queryset = NewsPost.objects.filter(featured=True)
#     serializer_class = NewsPostSerializer
#     lookup_field = 'slug'
#     permission_classes = (permissions.AllowAny,)