from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from entries.views import TextEntryViewSet

# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'text-entries', TextEntryViewSet, basename='text-entry')

# Define URL patterns
urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # API endpoints for text entries
    path('api/', include(router.urls)),

    # JWT authentication endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
