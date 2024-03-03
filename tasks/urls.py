from django.urls import path

from tasks import views
from tasks.views import IndexView, TagCreateView, TagUpdateView, TagDeleteView, TagListView, TaskCreateView, \
    TaskUpdateView, TaskDeleteView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="tag-delete"),
    path('tasks/<int:pk>/toggle/', views.toggle_task, name='toggle-task'),
]

app_name = "tasks"
