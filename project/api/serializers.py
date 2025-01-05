from rest_framework import serializers
from .models import User, Institute, Course, Review, Rating, Lesson
from django.core.validators import RegexValidator
from rest_framework_simplejwt.tokens import RefreshToken

username_validator = RegexValidator(
    regex=r'^[A-Za-zА-Яа-яЁё\s]+$',  # Разрешаем только заглавные буквы и символы
    message='Имя пользователя может содержать только строчные и заглавные буквы'
)

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[username_validator]  # Применяем валидатор к полю username
    )   
    
    class Meta:
        model = User
        fields = ['id','password', 'username', 'first_name', 'last_name', 'email', 'role']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            role=validated_data['role'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
            validated_data.pop('password')
        return super().update(instance, validated_data)

class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = ['id', 'name', 'rating']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'institute', 'teacher', 'schedule', 'settings']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'lesson', 'rating', 'comment', 'advantages', 'is_anonymous', 'created_at']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'course', 'average_rating', 'total_reviews', 'last_updated']

class LessonSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField(read_only=True)
    total_reviews = serializers.IntegerField(read_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'institute', 'course', 'teacher', 'topic', 'address', 'room', 'date', 'time', 'average_rating', 'total_reviews']
