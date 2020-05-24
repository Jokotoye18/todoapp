from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['title']
        labels = {"title":""}
        widgets = {"title":forms.TextInput(attrs={"placeholder":"What do you plan to do today?"})}


