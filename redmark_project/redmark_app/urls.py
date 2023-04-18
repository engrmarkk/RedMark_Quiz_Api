from django.urls import path
from .endpoints.questions import *
from .endpoints.options import *
from .endpoints.answers import *
from .endpoints.user.users import *
from .endpoints.user.auth import *


urlpatterns = [
    path("", QuestionView.as_view(), name="question"),
    path("<int:pk>/", EachQuestionView.as_view(), name="each_question"),
    path("options/", OptionView.as_view(), name="options"),
    path("options/<int:question_id>/", PostOptionView.as_view(), name="each_option"),
    path("answers/", AnswerView.as_view(), name="answer"),
    path("answers/<int:question_id>/", PostAnswerView.as_view(), name="post answer"),
    path("each-option/<int:pk>/", EachOptionView.as_view(), name="each option"),
    path("each-answer/<int:pk>/", EachAnswerView.as_view(), name="each answer"),
    path("all_users/", GetUsers.as_view(), name="all users"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
]
