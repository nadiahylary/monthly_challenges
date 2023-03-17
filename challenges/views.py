from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

from challenges.models import Challenge

monthly_challenges = {
    "january": "Maintain a morning routine for the entire month.",
    "february": "January Challenge + Exercise at least 20 minutes every day.",
    "march": "February Challenge + Wash & Fix your manicure/pedicure and hair every weekend.",
    "april": "March Challenge + Go to church every sunday + Pray every morning and night.",
    "may": "April Challenge + Don't touch your face + Speak affirmations everyday morning and evening.",
    "june": "May Challenge + Create Social media content on English for french speakers and mobile android "
            "development & flutter ""every weekend and post them during the week.",
    "july": "June Challenge + Learn German at least 4 hours every week.",
    "august": "July Challenge + Clean your belongings once a week.",
    "september": "August Challenge + Apply for remote jobs everyday.",
    "october": "September Challenge + Exercise at least 1 hour everyday.",
    "november": "October Challenge + Eat at least one fruit and one veggie everyday.",
    "december": None  # "November Challenge + Apply to at least 5 PFE internships offers every week."
}


# Create your views here.
def index(request):
    """
       response_data = ""
       for key in monthly_challenges.keys():
           month_path = reverse("month-challenge", args=[key])
           response_data += f"\n <li><a href = '{month_path}'>{key.capitalize()}</a></li>"
       response = f"<h1>My 2023 Monthly Challenges:</h1>\n<ul>{response_data}\n</ul>"
       return HttpResponse(response)"""
    challenges = monthly_challenges.items()
    months = monthly_challenges.keys()
    return render(request, "challenges/index.html", {
        "months": months,
        "challenges": challenges
    })


def monthly_challenges_by_num(request, month):
    months = list(monthly_challenges.keys())
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month": month,
            "challenge": challenge})
        # response_data = f"<h1>{challenge}</h1>"
        # response_data = render_to_string("challenges/challenge.html")
    except:
        raise Http404()


"""response_error_data = render_to_string("404.html")
    return HttpResponseNotFound(response_error_data)"""
# return HttpResponse(response_data)


"""
OR
    if month in monthly_challenges.keys():
        challenge = monthly_challenges[month]
    else:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(challenge)
"""

# TODO: Rewrite the views functions with datasource/storage
#  from the model & sqlite3 instead of the dictionary.


# def index_db(request):
#     challenges = Challenge.objects.all()
#     months = [month for month in challenges.objects.value_list('month')]
#     return render(request, "challenges/index.html", {
#         "months": months,
#         "challenges": challenges
#     })
#
#
# def monthly_challenges_db(request, month):
#     challenges = Challenge.objects.all()
#     months = [month for month in challenges.objects.value_list('month')]
#     redirect_month = months[month - 1]
#     redirect_path = reverse("month-challenge", args=[redirect_month])
#     return HttpResponseRedirect(redirect_path)
#
#
# def monthly_challenge_month_db(request, month):
#     try:
#         challenge = Challenge.objects.get(month=month)
#         return render(request, "challenges/challenge.html", {
#             "month": month,
#             "challenge": challenge})
#     except:
#         raise Http404()
