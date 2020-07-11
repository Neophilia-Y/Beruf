from django.urls import path
from products import views

app_name = "core"
urlpatterns = [path("", views.all_products, name="home")]

