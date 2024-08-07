from django.urls import path
from .views import UserView

app_name = "users"


urlpatterns = [
    path("", UserView.as_view(), name="user"),
    path("<int:pk>/", UserView.as_view(), name="user"),
]
