from django.urls import path
from .endpoints.questions import *
from .endpoints.options import *
from .endpoints.answers import *


urlpatterns = [
    path("", QuestionView.as_view(), name="index"),
    path("<int:pk>/", EachQuestionView.as_view(), name="each_question"),
    path("options/", OptionView.as_view(), name="options"),
    path("options/<int:pk>/", PostOptionView.as_view(), name="each_option"),
    path("answers/", AnswerView.as_view(), name="answer"),
    path("answers/<int:pk>/", PostAnswerView.as_view(), name="post answer"),
    path("each-option/<int:pk>/", EachOptionView.as_view(), name="each option")
]
