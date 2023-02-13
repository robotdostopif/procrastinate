from rest_framework import serializers
from tasks.models import Task, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title", "description")


class TaskSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Task
        fields = ("id", "title", "description", "priority", "category", "is_finished")
