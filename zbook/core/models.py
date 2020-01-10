from django.db import models

from zbook.system.models import BaseModel
from .choices import LocationType


class Location(BaseModel):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=16, null=True, blank=True)
    type = models.IntegerField(choices=LocationType.choices)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return ''


class Address(BaseModel):
    name = models.CharField(max_length=64)
    country = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='country_location')
    post_code = models.IntegerField(null=True, blank=True)
    state = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True, related_name='state_location')
    division = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True, related_name='division_location')
    district = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True, related_name='district_location')
    sub_district = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True, related_name='sub_district_location')
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return ''
