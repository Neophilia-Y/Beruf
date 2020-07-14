from django.urls import path
from products import views as products_view

app_name = "core"
urlpatterns = [
    path("", products_view.HomeView.as_view(), name="home"),
]

