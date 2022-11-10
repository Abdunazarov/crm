from django.urls import path
from .views import *


urlpatterns = [
    path('create/', create_news),
    path('detail/<pk>/', get_one_news),
    path('all/', ListNewsView.as_view()),
    path('update/<pk>/', update_news),
    path('delete/<pk>/', delete_news)

]