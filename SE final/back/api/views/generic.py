from django.http import JsonResponse
from api.models import Competition,Members
from api.serializers import CompetitionSerializer, MemberSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# def index(request):
#     comps=Competition.objects.all()
#     context=
#     return render (request,'index.html')

class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer


    # def get_queryset(self):
    #     return Competition.objects.for_user(self.request.user)

    def get_serializer_class(self):
        return CompetitionSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer

class CompetitionMember(generics.ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Members.objects.filter(comps=self.kwargs['pk'])

    def get_serializer_class(self):
        return MemberSerializer



class CompetitionMemberView(generics.RetrieveUpdateDestroyAPIView):

    #permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        print(self.kwargs)
        return Competition.objects.get(id=self.kwargs['pk']);

    def get_serializer_class(self):
        return CompetitionSerializer

