from rest_framework import generics # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework.views import APIView # type: ignore
from rest_framework import status # type: ignore
from .models import Task, User
from .serializers import TaskSerializer, AssignTaskSerializer


class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class AssignTaskView(APIView):
    def post(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
            serializer = AssignTaskSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Task assigned successfully"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)


class UserTasksView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            tasks = user.tasks.all()
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
