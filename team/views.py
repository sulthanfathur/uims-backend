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
        team_principal = TeamMember.objects.filter(jabatan="TEAM PRINCIPAL")
        team_principal_serializer = TeamMemberSerializer(team_principal, many=True)
        others = TeamMember.objects.filter(division="OTHERS").exclude(jabatan="TEAM PRINCIPAL")
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
    def get(self, request):
        gokart_team = TeamMember.objects.filter(division="GOKART")

        cto = gokart_team.filter(jabatan="CTO")
        cto_serializer = TeamMemberSerializer(cto, many=True)

        managers = gokart_team.filter(jabatan="MANAGER")
        managers_serializer = TeamMemberSerializer(managers, many=True)

        mechanics = gokart_team.filter(jabatan="MECHANIC")
        mechanics_serializer = TeamMemberSerializer(
            mechanics, many=True)

        response = {
            "status": 200,
            "message": "success",
            "cto": cto_serializer.data,
            "managers": managers_serializer.data,
            "mechanics": mechanics_serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)

class EVListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        ev_team = TeamMember.objects.filter(division="EV")

        cto = ev_team.filter(jabatan="CTO")
        cto_serializer = TeamMemberSerializer(cto, many=True)

        managers = ev_team.filter(jabatan="MANAGER")
        managers_serializer = TeamMemberSerializer(managers, many=True)

        mechanics = ev_team.filter(jabatan="MECHANIC")
        mechanics_serializer = TeamMemberSerializer(
            mechanics, many=True)

        response = {
            "status": 200,
            "message": "success",
            "cto": cto_serializer.data,
            "managers": managers_serializer.data,
            "mechanics": mechanics_serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)

class MarketingListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        marketing_team = TeamMember.objects.filter(division="MARKETING")

        cto = marketing_team.filter(jabatan="CTO")
        cto_serializer = TeamMemberSerializer(cto, many=True)

        managers = marketing_team.filter(jabatan="MANAGER")
        managers_serializer = TeamMemberSerializer(managers, many=True)

        staffs = marketing_team.filter(jabatan="STAFF")
        staffs_serializer = TeamMemberSerializer(
            staffs, many=True)

        response = {
            "status": 200,
            "message": "success",
            "cto": cto_serializer.data,
            "managers": managers_serializer.data,
            "staffs": staffs_serializer.data,
        }
        return Response(response, status=status.HTTP_200_OK)