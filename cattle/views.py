from rest_framework import generics
from .serializer import CattleSerializer
from .models import Cattle


class CattleList(generics.ListCreateAPIView):
    queryset = Cattle.objects.all()
    serializer_class = CattleSerializer


class CattleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cattle.objects.all()
    serializer_class = CattleSerializer