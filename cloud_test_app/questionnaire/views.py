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
    # Temporary values
    month_results = ["February: 1 (11.1%)",
                     "March: 1 (11.1%)"]
    day_results = ["Monday: 1 (11.1%)",
                   "Tuesday: 1 (11.1%)"]
    fav_results = ["February: Friday",
                   "March: Monday"]

    context = {"month_results": month_results,
        "day_results": day_results,
        "fav_results": fav_results,
    }
    return render(request, 'questionnaire/results.html', context)
