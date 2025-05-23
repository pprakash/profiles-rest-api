from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile-viewset', views.UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.UserLoginApiView.as_view()),
    path('hello-view', views.HelloApiView.as_view())
]