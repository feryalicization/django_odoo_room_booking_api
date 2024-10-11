from django.contrib import admin
from .models import Ruangan, Tipe, Lokasi, PemesananRuangan


@admin.register(Ruangan)
class RuanganAdmin(admin.ModelAdmin):
    list_display = ('nama', 'tipe', 'lokasi', 'kapasitas', 'created_at', 'updated_at')
    search_fields = ('nama', 'tipe__tipe', 'lokasi__lokasi')
    list_filter = ('tipe', 'lokasi', 'kapasitas', 'created_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at', 'deleted_at', 'created_by')
    fields = ('nama', 'tipe', 'lokasi', 'image', 'kapasitas', 'keterangan', 'created_at', 'updated_at', 'deleted_at', 'created_by')
    date_hierarchy = 'created_at'


@admin.register(Tipe)
class TipeAdmin(admin.ModelAdmin):
    list_display = ('tipe', 'created_at', 'updated_at')
    search_fields = ('tipe',)
    list_filter = ('tipe', 'created_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at', 'deleted_at', 'created_by')
    fields = ('tipe', 'created_at', 'updated_at', 'deleted_at', 'created_by')


@admin.register(Lokasi)
class LokasiAdmin(admin.ModelAdmin):
    list_display = ('lokasi', 'created_at', 'updated_at')
    search_fields = ('lokasi',)
    list_filter = ('lokasi', 'created_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at', 'deleted_at', 'created_by')
    fields = ('lokasi', 'created_at', 'updated_at', 'deleted_at', 'created_by')


@admin.register(PemesananRuangan)
class PemesananRuanganAdmin(admin.ModelAdmin):
    list_display = (
        'nomor_pemesanan',
        'ruangan',
        'nama_pemesanan',
        'tanggal_pemesanan',
        'status_pemesanan',
        'created_at',
        'updated_at'
    )
    search_fields = ('nomor_pemesanan', 'ruangan__nama', 'nama_pemesanan')
    list_filter = ('status_pemesanan', 'tanggal_pemesanan', 'ruangan__tipe', 'ruangan__lokasi', 'created_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at', 'deleted_at', 'created_by')
    fields = (
        'nomor_pemesanan',
        'ruangan',
        'nama_pemesanan',
        'tanggal_pemesanan',
        'status_pemesanan',
        'catatan_pemesanan',
        'created_at',
        'updated_at',
        'deleted_at',
        'created_by'
    )
    date_hierarchy = 'tanggal_pemesanan'
