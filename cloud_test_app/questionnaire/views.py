from django.db.models import Count
from django.shortcuts import redirect, render
from questionnaire.models import FilledQuestionnaire
from questionnaire.forms import QuestionnaireForm
from questionnaire.models import DAYS_DICT, MONTHS_DICT


def index(request):
    # Count all the answers in the FilledQuestionnaire database.
    num_answers = FilledQuestionnaire.objects.count()
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
           # Save the ModelForm data to the database model.
           form.save()
           return redirect("index")

    else:
        form = QuestionnaireForm()

    context = {'form': form}
    return render(request, 'questionnaire/questionnaire.html', context)


def results(request):
    # TODO: Fill out database and result logic here
    # Temporary values
    FQ_model = FilledQuestionnaire
    num_answers = FilledQuestionnaire.objects.count()

    month_results = []
    for month_num in range(1, 13):
        month_count = FQ_model.objects.filter(month=month_num).count()
        if month_count != 0:
            month_frac = month_count/num_answers
            month_results.append(
                 f"{MONTHS_DICT[month_num]:s}: {month_count:d} ({month_frac:3.1%})")
        else:
            continue

    day_results = []
    for day_num in range(1, 8):
        day_count = FQ_model.objects.filter(day=day_num).count()
        if day_count != 0:
            day_frac = day_count/num_answers
            day_results.append(
                 f"{DAYS_DICT[day_num]:s}: {day_count:d} ({day_frac:3.1%})")
        else:
            continue

    fav_results = []
    for month_num in range(1, 13):
        # For a given month count the number of ids for each unique day, then order by the frequency.
        ordered_fav_days = FQ_model.objects.filter(month=month_num
            ).values("day"
            ).annotate(day_count=Count("id")
            ).order_by("-day_count")
        if len(ordered_fav_days) != 0:
            fav_day = ordered_fav_days[0]["day"]
            fav_results.append(
                 f"{MONTHS_DICT[month_num]:s}: {DAYS_DICT[fav_day] :s}")
        else:
            continue

    context = {"month_results": month_results,
        "day_results": day_results,
        "fav_results": fav_results,
    }
    return render(request, 'questionnaire/results.html', context)
