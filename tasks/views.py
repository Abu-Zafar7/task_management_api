from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Task, User
from .serializers import TaskSerializer, UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=['post'])
    def assign_users(self, request, pk = None): 
        task = self.get_object()
        user_ids = request.data.get('user_ids', [])

        if not isinstance(user_ids, list):
            return Response({'error': 'user_ids must be a list'}, status=status.HTTP_400_BAD_REQUEST)
        users = User.objects.filter(id__in=user_ids)
        
        if not users.exists():
            return Response({'error': 'No valid users found'}, status=status.HTTP_400_BAD_REQUEST)
        
        task.assigned_users.add(*users)
        
        return Response(
            {'message': f'Successfully assigned users to task {task.name}'},status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'], url_path='user/(?P<user_id>\d+)')
    def user_tasks(self, request, user_id = None):
        user = get_object_or_404(User, id = user_id)     
        tasks = user.tasks.all()
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)

    def perform_update(self, serializer):
        instance = serializer.instance
        new_status = serializer.validated_data.get('status')
        
        update_data = {}

        if new_status == 'COMPLETED' and instance.status != 'COMPLETED':
            update_data['completed_at'] = timezone.now()  
        elif new_status != 'COMPLETED' and instance.status == 'COMPLETED':
            update_data['completed_at'] = None  

        serializer.save(**update_data) 
