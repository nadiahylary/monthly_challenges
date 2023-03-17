from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index_db, name="index"),
    # path("<int:month>", views.monthly_challenges_db),
    # path("<str:month>", views.monthly_challenge_month_db, name="month-challenge")
    path("", views.index, name="index"),
    path("<int:month>", views.monthly_challenges_by_num),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]
