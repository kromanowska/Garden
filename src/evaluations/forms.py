from django import forms
from departments import models


class EvaluationSearchForm(forms.Form):
    name = forms.CharField(max_length=256, required=False)
    submited_from = forms.DateField(required=False)
    submited_to = forms.DateField(required=False)
    department = forms.ModelChoiceField(
        queryset=models.Departments.objects.all(),
        empty_label='All departments',
        required=False
    )
