from django import forms
from django import forms
from django.db.models import fields
from .models import Todo

class TodoAddForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title',)

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'completed')

