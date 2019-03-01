from django.shortcuts import render
from questionnaire.models import FilledQuestionnaire

def index(request):
    # Count all the answers in the FilledQuestionnaire database.
    num_answers = FilledQuestionnaire.objects.all().count()
    context = {
        'title': "Basic Questions!",
        'num_answers': num_answers,
    }
    return render(request, 'questionnaire/index.html', context)

def questionnaire(request):
    # TODO: Add form POST/GET logic
    return render(request, 'questionnaire/questionnaire.html')
