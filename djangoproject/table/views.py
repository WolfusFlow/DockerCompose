# from django.shortcuts import render
from table.serializers import TableSerializer
from table.models import valueTable
from rest_framework import generics

class tableListCreate(generics.ListCreateAPIView):
   queryset = valueTable.objects.all()
   serializer_class = TableSerializer