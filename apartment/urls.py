from pydoc import getpager
from django.urls import path
from .views import *

urlpatterns = [
    path('create/', create_apartment),
    path('all/', get_apartments),
    path('<pk>/', detail_apartment),
    path('update/<pk>/', update_apartment),
    path('delete/<pk>/', delete_apartment)

]