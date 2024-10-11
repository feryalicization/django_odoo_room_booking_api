import django_filters
from ..models import Ruangan, Tipe, Lokasi

class RuanganFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(field_name='nama', lookup_expr='icontains', label='Search')
    tipe = django_filters.ModelChoiceFilter(queryset=Tipe.objects.all(), label='Tipe')
    lokasi = django_filters.ModelChoiceFilter(queryset=Lokasi.objects.all(), label='Lokasi')

    class Meta:
        model = Ruangan
        fields = ['search', 'tipe', 'lokasi']
