from django import forms
from common import enums


class DepartmentsSearchForm(forms.Form):
    IS_ACTIVE_CHOICES = (
        (enums.IsActiveSearchEnum.ALL.value, 'All statuses'),
        (enums.IsActiveSearchEnum.ACTIVE.value, 'Active'),
        (enums.IsActiveSearchEnum.INACTIVE.value, 'Inactive'),
    )
    name = forms.CharField(max_length=256)
    abbreviation = forms.CharField(max_length=10)
    is_active = forms.ChoiceField(choices=IS_ACTIVE_CHOICES, initial=enums.IsActiveSearchEnum.ACTIVE.value)
    manager = forms.CharField(max_length=256)
    deputy_manager = forms.CharField(max_length=256)
