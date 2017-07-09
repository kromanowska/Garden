from django import forms
from common import enums
from phonenumber_field import formfields
from departments import models


class UserSearchForm(forms.Form):
    IS_ACTIVE_CHOICES = (
        (enums.IsActiveSearchEnum.ALL.value, 'All'),
        (enums.IsActiveSearchEnum.ACTIVE.value, 'Active'),
        (enums.IsActiveSearchEnum.INACTIVE.value, 'Inactive'),
    )
    name = forms.CharField(max_length=256, required=False)
    email = forms.EmailField(required=False)
    phone = formfields.PhoneNumberField(required=False)
    department = forms.ModelChoiceField(
        queryset=models.Departments.objects.filter(is_active=True),
        empty_label='All',
        required=False
    )
    is_active = forms.ChoiceField(choices=IS_ACTIVE_CHOICES, initial=enums.IsActiveSearchEnum.ACTIVE.value)
