from django import forms
from django.contrib.auth.models import User

class AddMembersForm(forms.Form):
    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select'}),
    )