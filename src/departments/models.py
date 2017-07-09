from django.db import models


class Departments(models.Model):
    name = models.CharField(max_length=256, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=True)
    manager = models.OneToOneField('auth.User', related_name='managed_department')
    deputy_manager = models.OneToOneField('auth.User', blank=True, null=True, related_name='managed_department_deputy')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
