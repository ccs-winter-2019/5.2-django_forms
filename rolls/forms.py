from django.forms import ModelForm

from .models import Roll


class RollCreateForm(ModelForm):

    class Meta:
        model = Roll
        fields = ['title', 'year_made', 'image', ]