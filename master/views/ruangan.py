from rest_framework import generics
from ..models import Ruangan
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from ..serializers.ruangan import RuanganUpdateDeleteCreateSerializer, RuanganListDetailSerializer
from ..filter.ruangan import RuanganFilter  
from django.utils import timezone



class RuanganCreateView(generics.CreateAPIView):
    serializer_class = RuanganUpdateDeleteCreateSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class RuanganListView(generics.ListAPIView):
    queryset = Ruangan.objects.filter(deleted_at__isnull=True)  
    serializer_class = RuanganListDetailSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RuanganFilter  

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class RuanganDetailView(generics.RetrieveAPIView):
    queryset = Ruangan.objects.filter(deleted_at__isnull=True)
    serializer_class = RuanganListDetailSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class RuanganUpdateDeleteAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Ruangan.objects.filter(deleted_at__isnull=True)
    serializer_class = RuanganUpdateDeleteCreateSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted_at = timezone.now()  
        instance.deleted_by = request.user  
        instance.save() 
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save(updated_at=timezone.now(), updated_by=self.request.user)
