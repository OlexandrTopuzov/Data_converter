from django.db import models

from data_ocean.models import DataOceanModel


class KoatuuCategory(DataOceanModel):
    name = (models.CharField(max_length=5, unique=True, null=True))


class KoatuuRegion(DataOceanModel):
    name = models.CharField(max_length=30, unique=True)
    code = models.CharField(max_length=10, unique=True, null=True)


class KoatuuDistrict(DataOceanModel):
    region = models.ForeignKey(KoatuuRegion, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True, null=True)


class KoatuuCity(DataOceanModel):
    region = models.ForeignKey(KoatuuRegion, on_delete=models.CASCADE)
    district = models.ForeignKey(KoatuuDistrict, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(KoatuuCategory, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True, null=True)


class KoatuuCityDistrict(DataOceanModel):
    region = models.ForeignKey(KoatuuRegion, on_delete=models.CASCADE)
    district = models.ForeignKey(KoatuuDistrict, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(KoatuuCity, on_delete=models.CASCADE)
    category = models.ForeignKey(KoatuuCategory, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True, null=True)
