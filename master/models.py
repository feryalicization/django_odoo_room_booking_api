from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils import timezone


class BaseModels(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True



class Ruangan(BaseModels):
    nama = models.CharField(max_length=255, null=True, blank=True, verbose_name="Nama Ruangan")
    tipe = models.ForeignKey('Tipe', on_delete=models.CASCADE, null=True, blank=True)
    lokasi = models.ForeignKey('Lokasi', on_delete=models.CASCADE, null=True, blank=True)
    image = models.FileField(verbose_name="Image", blank=False, null=True, upload_to="images")
    kapasitas = models.IntegerField(null=True, blank=True, verbose_name="Kapasitas")
    keterangan = models.TextField(verbose_name="Keterangan", blank=True)

    def __str__(self):
        return self.nama



class Tipe(BaseModels):
    TIPE_CHOICE = (
        ("Meeting Room Kecil", "Meeting Room Kecil"),
        ("Meeting Room Besar", "Meeting Room Besar"),
        ("Aula", "Aula"),
    )
    tipe = models.CharField(max_length=255, null=True, blank=True, verbose_name="Tipe", choices=TIPE_CHOICE)

    def __str__(self):
        return self.tipe


class Lokasi(BaseModels):
    LOKASI_CHOICE = (
        ("1A", "1A"),
        ("1B", "1B"),
        ("1C", "1C"),
        ("2A", "2A"),
        ("2B", "2B"),
        ("2C", "2C"),
    )
    lokasi = models.CharField(max_length=255, null=True, blank=True, verbose_name="Lokasi", choices=LOKASI_CHOICE)

    def __str__(self):
        return self.lokasi


class PemesananRuangan(BaseModels):
    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('On Going', 'On Going'),
        ('Done', 'Done'),
        ('Canceled', 'Canceled'),
    )

    nomor_pemesanan = models.CharField(max_length=255, unique=True, verbose_name="Nomor Pemesanan")  
    ruangan = models.ForeignKey('Ruangan', on_delete=models.CASCADE, verbose_name="Ruangan")  
    nama_pemesanan = models.CharField(max_length=255, verbose_name="Nama Pemesanan")  
    tanggal_pemesanan = models.DateField(default=timezone.now, verbose_name="Tanggal Pemesanan")  
    status_pemesanan = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='Draft',
        verbose_name="Status Pemesanan"
    )  
    catatan_pemesanan = models.TextField(blank=True, null=True, verbose_name="Catatan Pemesanan")  

    def __str__(self):
        return f'Pemesanan {self.nomor_pemesanan} - {self.nama_pemesanan}'
    
    def save(self, *args, **kwargs):
        if not self.nomor_pemesanan:
            tipe = self.ruangan.tipe.tipe[:3].upper()
            ruangan = self.ruangan.nama[:3].upper()
            date_str = timezone.now().strftime('%Y%m%d')
            sequence = uuid.uuid4().hex[:6].upper()
            self.nomor_pemesanan = f"{tipe}-{ruangan}-{date_str}-{sequence}"
        super(PemesananRuangan, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Pemesanan Ruangan"
        verbose_name_plural = "Pemesanan Ruangan"
        ordering = ['-tanggal_pemesanan']
