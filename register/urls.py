from .views import ProfileList,RegisterAPI,LoginAPI,UserAPI
from django.urls import path
from knox import views as knox_views


urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('profile/', ProfileList.as_view(), name='profiles'),
    path('user/', UserAPI.as_view()),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
