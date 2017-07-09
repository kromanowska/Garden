import os
import uuid

from django.db import models
from phonenumber_field import modelfields
from users import enums


def get_upload_path(instance, filename):
    return os.path.join('photos', uuid.uuid1().hex + os.path.splitext(filename)[1])


class Profile(models.Model):
    EDUCATION_CHOICES = (
        (enums.EducationEnum.NONE.value, 'None'),
        (enums.EducationEnum.ELEMENTARY_SCHOOL.value, 'Elementary school'),
        (enums.EducationEnum.MIDDLE_SCHOOL.value, 'Middle school'),
        (enums.EducationEnum.HIGH_SCHOOL.value, 'High school'),
    )
    landline_phone = modelfields.PhoneNumberField(blank=True)
    cell_phone = modelfields.PhoneNumberField(blank=True)
    certificates = models.TextField(blank=True)
    other_skills = models.TextField(blank=True)
    photo = models.ImageField(upload_to=get_upload_path, blank=True)
    education = models.IntegerField(choices=EDUCATION_CHOICES)
    department = models.ForeignKey('departments.Departments', related_name='profiles')
    languages = models.ManyToManyField('Language', related_name='profiles')
    driving_licences = models.ManyToManyField('DrivingLicence', related_name='profiles', blank=True)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.user.get_full_name()


class Language(models.Model):
    name = models.CharField(max_length=64)
    abbreviation = models.CharField(max_length=8)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class DrivingLicence(models.Model):
    VEHICLE_TYPE_CHOICES = (
        (enums.VehicleTypeEnum.MOPED.value, 'Moped'),
        (enums.VehicleTypeEnum.MOTORCYCLE.value, 'Motorcycle'),
        (enums.VehicleTypeEnum.MOTOR_VEHICLE.value, 'Motor vehicle'),
        (enums.VehicleTypeEnum.LARGE_GOODS_VEHICLE.value, 'Large goods vehicle'),
        (enums.VehicleTypeEnum.BUS.value, 'Bus'),
    )
    class_name = models.CharField(max_length=8)
    vehicle_type = models.IntegerField(choices=VEHICLE_TYPE_CHOICES)
    description = models.TextField()

    class Meta:
        ordering = ['class_name']

    def __str__(self):
        return self.class_name
