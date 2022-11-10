from django.urls import path
from .views import *


urlpatterns = [
    path('number_active/', count_active),
    path('number_warm/', count_warm),
    path('number_hot/', count_hot),
    path('bez_vnimaniya/', bez_vnimaniya),
    path('all_requests/', all_requests)

]