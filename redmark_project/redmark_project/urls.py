from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("redmark_app.urls")),
    path("/<int:pk>/", include("redmark_app.urls")),
    path("options/", include("redmark_app.urls")),
    path("options/<int:pk>/", include("redmark_app.urls")),
    path("answers/", include("redmark_app.urls")),
    path("answers/<int:pk>/", include("redmark_app.urls")),
    path("each-option/<int:pk>/", include("redmark_app.urls")),
    path("all_users/", include("redmark_app.urls")),
    path("register/", include("redmark_app.urls")),
    path("login/", include("redmark_app.urls")),
    path("logout/", include("redmark_app.urls")),
]
