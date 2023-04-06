# from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", include("redmark_app.urls")),
    path("/<int:pk>/", include("redmark_app.urls")),
    path("options/", include("redmark_app.urls")),
    path("options/<int:pk>/", include("redmark_app.urls")),
    path("answers/", include("redmark_app.urls")),
    path("answers/<int:pk>/", include("redmark_app.urls")),
    path("each-option/<int:pk>/", include("redmark_app.urls"))
]
