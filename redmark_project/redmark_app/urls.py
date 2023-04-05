from django.urls import path
# from .views import IndexView
from .endpoints.questions import IndexView



urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]