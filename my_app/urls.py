from django.urls import path

from my_app.views import hi_world, hello_world, person_info, person_search

urlpatterns = [
    path('hi', hi_world),
    path('hello_world', hello_world),
    path('person-info/<int:person_id>', person_info),
    path('person-search/<str:person_name>', person_search)
]