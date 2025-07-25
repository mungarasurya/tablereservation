"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
# main url routes developments 
from application.views import CustomTokenObtainPairView
from rest_framework.routers import DefaultRouter
from application.views import UserViewSet, RestaurantViewSet, BookingViewSet, WishlistViewSet, AlertViewSet

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'restaurants', RestaurantViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'wishlist', WishlistViewSet)
router.register(r'alerts', AlertViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/',CustomTokenObtainPairView.as_view(),name='get_token'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='refresh_token'),
    #main path developments 
    path('api/', include(router.urls)),
]
