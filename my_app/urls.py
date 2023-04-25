from django.urls import path

from my_app.views import hi_world, hello_world

urlpatterns = [
    path('hi', hi_world),
    path('hello_world', hello_world),
]