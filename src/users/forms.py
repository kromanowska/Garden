from django.contrib.auth import forms as auth_forms
from django.contrib.auth import models as auth_models
from django import forms
from common import enums
from phonenumber_field import formfields
from users import models as users_models
from departments import models as departments_models


class UserSearchForm(forms.Form):
    IS_ACTIVE_CHOICES = (
        (enums.IsActiveSearchEnum.ALL.value, 'All statuses'),
        (enums.IsActiveSearchEnum.ACTIVE.value, 'Active'),
        (enums.IsActiveSearchEnum.INACTIVE.value, 'Inactive'),
    )
    name = forms.CharField(max_length=256, required=False)
    job = forms.CharField(max_length=256, required=False)
    email = forms.EmailField(required=False)
    phone = formfields.PhoneNumberField(required=False)
    department = forms.ModelChoiceField(
        queryset=departments_models.Departments.objects.all(),
        empty_label='All departments',
        required=False
    )
    is_active = forms.ChoiceField(choices=IS_ACTIVE_CHOICES, initial=enums.IsActiveSearchEnum.ACTIVE.value)


class UserCreateForm(auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

    class Meta:
        model = auth_models.User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']
        field_classes = {'username': auth_forms.UsernameField}


class UserUpdateForm(auth_forms.UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.fields['password'].disabled = True
        self.fields['date_joined'].disabled = True
        self.fields['is_superuser'].disabled = True
        self.fields['is_staff'].disabled = True


class ProfileForm(forms.ModelForm):
    class Meta:
        model = users_models.Profile
        fields = ['landline_phone', 'cell_phone', 'job', 'hire_date', 'department', 'photo', 'education',
                  'languages', 'driving_licences', 'certificates', 'other_skills']
