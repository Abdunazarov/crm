from django.urls import path
from .views import *


urlpatterns = [
    path('all/', ListRequestsView.as_view()),
    path('create/', create_request),
    path('update/<pk>/', update_request),
    path('delete/<pk>/', delete_request),
    path('detail/<pk>/', get_one_request)

]