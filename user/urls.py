from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path('register/', register_rieltor),
    path('login/', obtain_auth_token),
    path('profile/', profile),
    path('update/', update_user),

    path('all/', all_users),
]