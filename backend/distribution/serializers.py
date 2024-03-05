from rest_framework import serializers
from .models import Student, Product, Lesson, Group, Author

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'id',
            'student_name',
            'slug',
            'product',
            'is_addmitted',
        ]
        model = Student

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
                  'author',
                  'product_name',
                  'started',
                  'cost',
                  'min_student_amount',
                  'max_student_amount',
        ]
        model = Product

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'lesson_name',
            'video_link',
            'product',
        ]
        model = Lesson

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'students',
            'group_name',
            'product',
        ]
        model = Group

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'author_name',
        ]
        model = Author
