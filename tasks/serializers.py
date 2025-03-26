from rest_framework import serializers
from .models import Task, User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'mobile', 'password']


class TaskSerializer(serializers.ModelSerializer):
    assigned_users = UserSerializer(many=True, read_only=True)
    assigned_users_ids = serializers.PrimaryKeyRelatedField(
        many = True,
        write_only = True,
        queryset = User.objects.all(),
        source='assigned_users'
    )

    class Meta:
        model = Task
        fields = ['id', 'name', 'description','created_at','task_type','completed_at','status', 'assigned_users', 'assigned_users_ids']
        read_only_fields = ['id', 'created_at', 'assigned_users','completed_at']