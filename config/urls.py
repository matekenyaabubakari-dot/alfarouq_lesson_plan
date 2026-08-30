from django.contrib import admin
from django.urls import path

from lessonplan import views


urlpatterns = [

    path(
        "admin/",
        admin.site.urls
    ),

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "create/",
        views.create_lesson_plan,
        name="create_lesson_plan"
    ),

    path(
        "lesson-plans/",
        views.lesson_plan_list,
        name="lesson_plan_list"
    ),

    path(
        "lesson-plan/<int:pk>/",
        views.lesson_plan_detail,
        name="lesson_plan_detail"
    ),

    path(
        "lesson-plan/<int:pk>/edit/",
        views.edit_lesson_plan,
        name="edit_lesson_plan"
    ),

    path(
        "lesson-plan/<int:pk>/delete/",
        views.delete_lesson_plan,
        name="delete_lesson_plan"
    ),

    path(
        "reports/",
        views.reports,
        name="reports"
    ),

    path(
        "profile/",
        views.profile,
        name="profile"
    ),

    path(
        "settings/",
        views.settings,
        name="settings"
    ),
]