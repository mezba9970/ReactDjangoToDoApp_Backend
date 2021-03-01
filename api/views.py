from django.shortcuts import render
from .models import Plan
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView
from .serializers import PlanSerializer

# Create your views here.

class PlanList(ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class PlanCreate(CreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class PlanDelete(DestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    lookup_field = 'id'

