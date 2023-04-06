from django.urls import path
# from .views import IndexView
from .endpoints.questions import *
from .endpoints.options import *


urlpatterns = [
    path("", QuestionView.as_view(), name="index"),
    path("<int:pk>/", EachQuestionView.as_view(), name="each_question"),
    path("options/", OptionView.as_view(), name="options"),
    path("options/<int:pk>/", EachOptionView.as_view(), name="each_option"),
]
