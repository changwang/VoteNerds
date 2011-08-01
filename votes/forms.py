from django import forms

class GameBoughtForm(forms.Form):
    games = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)
