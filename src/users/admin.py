from django.contrib import admin
from users import models

admin.site.register(models.Profile)
admin.site.register(models.Language)
admin.site.register(models.DrivingLicence)
