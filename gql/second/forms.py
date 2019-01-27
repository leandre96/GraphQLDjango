from django.forms import ModelForm
from .models import Animal

# Create the form class.
class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'genus', 'is_domesticated']
