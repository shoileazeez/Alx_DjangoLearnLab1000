from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'my-models', BookViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]