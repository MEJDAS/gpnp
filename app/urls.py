from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("team-menu", views.teamMenu, name="team-menu"),
    path("request-menu", views.requestMenu, name="request-menu"),
    path("report-menu", views.reportMenu, name="report-menu"),
     path("departement", views.departement, name="departement"),



]
