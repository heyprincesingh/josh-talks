from django.urls import path # type: ignore
from .views import TaskCreateView, AssignTaskView, UserTasksView

urlpatterns = [
    path('tasks/create/', TaskCreateView.as_view(), name='create_task'),
    path('tasks/assign/<int:task_id>/', AssignTaskView.as_view(), name='assign_task'),
    path('tasks/user/<int:user_id>/', UserTasksView.as_view(), name='user_tasks'),
]
