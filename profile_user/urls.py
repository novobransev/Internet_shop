from django.urls import path

from .views import ProfileView, ProfileUpdateView

urlpatterns = [
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('update_profile/<int:pk>/', ProfileUpdateView.as_view(), name='update_profile'),
]
