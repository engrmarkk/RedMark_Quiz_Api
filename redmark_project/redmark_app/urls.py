from django.urls import path
# from .views import IndexView
from .endpoints.questions import *



urlpatterns = [
    path("", QuestionView.as_view(), name="index"),
]