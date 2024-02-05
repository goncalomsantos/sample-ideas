from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("weight_tracker/", include("weight_tracker.urls")),
    path("admin/", admin.site.urls),
]