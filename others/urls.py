from django.urls import path
from .views import *


urlpatterns = [
    path('analitika/', analytics_count),
    path('vse_zayavki/', all_requests)

]