from django.urls import path

from vote import views

urlpatterns = [
    path('',views.vote_fun,name="vote")
    ]