from django import forms
from . import models


class searchForm(forms.Form):

    title = forms.CharField(required=False)
    category = forms.ModelChoiceField(
        queryset=models.Category.objects.all(),
        empty_label="select category",
        required=True,
    )
    price = forms.IntegerField(required=False)
    condition = forms.ModelMultipleChoiceField(
        queryset=models.Condition.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )
