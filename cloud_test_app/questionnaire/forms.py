from django import forms


class QuestionnaireForm(forms.Form):
    month = forms.IntegerField()
    day = forms.IntegerField()
