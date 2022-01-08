from django.urls import path
from . import views

app_name = "manchete"

urlpatterns = [

    path("", views.PostList.as_view(),name="list"),
    path("<slug:slug>/", views.PostDetailView.as_view(), name="detail"), 

]