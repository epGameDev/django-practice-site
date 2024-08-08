from django.urls import path;

from . import views; # The dot states "from this module or folder"

urlpatterns = [
  path('', views.index),
  path("<str:month>/", views.monthly_challenge ),
]