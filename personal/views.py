from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Departman, Personal
from .serializers import DepartmanSerializer, PersonalSerializer
from .permissions import IsStaffOrReadOnly, IsOwnerAndStaffOrReadOnly


class DepartmanListCreateAPIView(ListCreateAPIView):
    queryset = Departman.objects.all()
    serializer_class = DepartmanSerializer
    permission_classes = [IsAuthenticated, IsStaffOrReadOnly]


class DepartmanDetail(RetrieveUpdateDestroyAPIView):
    queryset = Departman.objects.all()
    serializer_class = DepartmanSerializer
    permission_classes = [IsAuthenticated, IsStaffOrReadOnly]



class PersonalListCreateAPIView(ListCreateAPIView):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer
    permission_classes = [IsAuthenticated, IsStaffOrReadOnly]


class PersonalDetail(RetrieveUpdateDestroyAPIView):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer
    permission_classes = [IsAuthenticated, IsOwnerAndStaffOrReadOnly]