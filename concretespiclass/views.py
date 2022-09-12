from django.shortcuts import render
from .models import student
from .serializer import s_serializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView


class studentlistcreate(ListCreateAPIView):
    queryset=student.objects.all()
    serializer_class = s_serializer

class studentretrieveupdatedestroy(RetrieveUpdateDestroyAPIView):
    queryset = student.objects.all()
    serializer_class = s_serializer



