from django.urls import path
from .views import CompliantView


app_name = "main"

urlpatterns = [
    path("", CompliantView.as_view(), name=""),
    path("<int:pk>/", CompliantView.as_view(), name=""),
]
