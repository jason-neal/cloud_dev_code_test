from django import forms
from questionnaire.models import FilledQuestionnaire


class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = FilledQuestionnaire
        fields = '__all__'
