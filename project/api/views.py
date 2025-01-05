from django.shortcuts import render

from rest_framework import viewsets
from .models import User, Institute, Course, Review, Rating, Lesson
from .serializers import UserSerializer, InstituteSerializer, CourseSerializer, ReviewSerializer, RatingSerializer, LessonSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class InstituteViewSet(viewsets.ModelViewSet):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

from rest_framework import filters

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['lesson__id']

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
