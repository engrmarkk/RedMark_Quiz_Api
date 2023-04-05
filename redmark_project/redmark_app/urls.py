from django.urls import path
# from .views import IndexView
from .endpoints.questions import *


urlpatterns = [
    path("", QuestionView.as_view(), name="index"),
    path("<int:pk>/", EachQuestionView.as_view(), name="each_question"),
]
