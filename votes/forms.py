from django import forms

class GameBoughtForm(forms.Form):
    """
    form is uesed to generate multiple selection form.
    """
    games = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)
