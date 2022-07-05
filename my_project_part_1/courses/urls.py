from courses import views
from django.urls import path

# TODO настройте здесь urls для заданий сourses, new_courses, find_by_name, who's_author
urlpatterns = [
    path("", views.courses, name="courses_list"),
    path("new/", views.new_courses, name="new_courses"),
    path("search/", views.search, name="courses_search"),
    path("<slug:slug>/", views.get_course, name="get_course"),
]
