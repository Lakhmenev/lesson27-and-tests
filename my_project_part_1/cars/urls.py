from cars import views
from django.urls import path


# TODO настройте здесь urls для заданий get_car и search_car)
urlpatterns = [
    path("<int:pk>/", views.get_car, name="car"),
    path("search/", views.search, name="cars_search"),
]

