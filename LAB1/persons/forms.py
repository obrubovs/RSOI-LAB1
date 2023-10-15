from .models import Person
from django.forms import ModelForm, TextInput, NumberInput


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age', 'address', 'work']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            'Возраст': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст'
            }),
            'address': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес'
            }),
            'work': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Работа'
            }),
        }