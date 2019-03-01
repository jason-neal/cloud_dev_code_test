from django.shortcuts import render, redirect
from questionnaire.models import FilledQuestionnaire
from questionnaire.forms import QuestionnaireForm

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
    if request.method == "POST":

        form = QuestionnaireForm(request.POST)
        if form.is_valid():
           # TODO: Save the data to database model
           redirect('index')
    else:
        form = QuestionnaireForm()

    context = {'form': form}
    return render(request, 'questionnaire/questionnaire.html', context)


def results(request):
    # TODO: Fill out database and result logic here
    return render(request, 'questionnaire/results.html')
