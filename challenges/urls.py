from django.urls import path

from . import views; # The dot states "from this module or folder"

urlpatterns = [
  path('', views.index),
  path("<int:month>/", views.monthly_challenge_index ),
  path("<str:month>/", views.monthly_challenge ),
]