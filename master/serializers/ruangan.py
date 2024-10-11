from rest_framework import serializers
from ..models import Ruangan
from django.utils import timezone

class RuanganUpdateDeleteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruangan
        fields = ['id', 'nama', 'tipe', 'lokasi', 'image', 'kapasitas', 'keterangan']

    def delete(self, instance):
        instance.deleted_at = timezone.now()
        instance.deleted_by = self.context['request'].user
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.updated_at = timezone.now()
        instance.updated_by = self.context['request'].user
        instance.save()
        return instance

    def create(self, validated_data):
        ruangan = Ruangan.objects.create(
            **validated_data, 
            created_by=self.context['request'].user  
        )
        return ruangan


class RuanganListDetailSerializer(serializers.ModelSerializer):
    tipe = serializers.CharField(source='tipe.tipe', read_only=True)  
    lokasi = serializers.CharField(source='lokasi.lokasi', read_only=True) 

    class Meta:
        model = Ruangan
        fields = ['id', 'nama', 'tipe', 'lokasi', 'image', 'kapasitas', 'keterangan']  

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation
