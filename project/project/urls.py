from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import UserViewSet, InstituteViewSet, CourseViewSet, ReviewViewSet, RatingViewSet, CustomTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'institutes', InstituteViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'ratings', RatingViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="GeeseRate API",
        default_version='v1',
        description="API чтоб было по кайфу",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="queniiikio@qwekio.ru"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
