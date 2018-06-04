from django.urls import path

from . import views

app_name = "core"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("details/<int:pk>", views.ProductDetailView.as_view(), name="details"),
    path("tv", views.TvListView.as_view(), name="tv_list"),
    path("fridge", views.FridgeListView.as_view(), name="fridge_list"),
    path("inc-click/<int:pk>", views.increase, name="increase-clicks"),
]