from django.urls import path, include
from . import views

urlpatterns = [
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('profile/<slug:username>', views.profile, name='profile')
]