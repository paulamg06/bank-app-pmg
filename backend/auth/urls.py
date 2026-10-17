from django.urls import path
from .views import register_user, login_user, actual_user, logout_user, csrf

urlpatterns = [
    path('register/', register_user),
    path('login/', login_user),
    path('me/', actual_user),
    path('logout/', logout_user),
    path('csrf/', csrf),
]