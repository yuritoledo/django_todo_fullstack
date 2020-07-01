from django import forms


class TodoForm(forms.Form):
    text = forms.CharField(max_length=20)
    completed = forms.BooleanField(required=False)
