from django.urls import path
from django.urls.conf import include
from django.urls import path, include
from .views import helloAPI, quizList

urlpatterns = [
    path("hello/", helloAPI),
    path("<int:id>/", quizList),
]