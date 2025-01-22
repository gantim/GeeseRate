import qrcode
import io
from django.shortcuts import render
from django.core.cache import cache  # Для хранения данных о сроке действия QR-кода
from django.http import HttpResponse

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime, timedelta
from .models import User, Institute, Course, Review, Rating, Lesson
from .serializers import UserSerializer, InstituteSerializer, CourseSerializer, ReviewSerializer, RatingSerializer, LessonSerializer, QRCodeSerializer

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

class QRCodeView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = QRCodeSerializer(data=request.data)
        if serializer.is_valid():
            link = serializer.validated_data['link']
            expiration_time = serializer.validated_data['expiration_time']
            time_unit = serializer.validated_data['time_unit']

            # Конвертируем время в секунды
            if time_unit == 'seconds':
                timeout = expiration_time
            elif time_unit == 'minutes':
                timeout = expiration_time * 60
            elif time_unit == 'hours':
                timeout = expiration_time * 3600

            # Генерация QR-кода
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(link)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)

            # Сохраняем QR-код и время действия в кэше
            qr_key = f"qr_{datetime.now().timestamp()}"
            cache.set(qr_key, {"link": link}, timeout=timeout)

            # Возвращаем QR-код в виде изображения
            return Response({
                "qr_key": qr_key,
                "qr_code_url": request.build_absolute_uri(f"/api/qr/{qr_key}/"),
                "expiration_time": f"{expiration_time} {time_unit}"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class QRCodeRetrieveView(APIView):
    def get(self, request, qr_key, *args, **kwargs):
        qr_data = cache.get(qr_key)
        if qr_data:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(qr_data['link'])
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)

            return HttpResponse(buffer, content_type="image/png")
        return Response({"detail": "QR-code expired or not found"}, status=status.HTTP_404_NOT_FOUND)