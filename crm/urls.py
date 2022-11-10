from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('apartment/', include('apartment.urls')),
    path('request_sell/', include('request_sell.urls')),
    path('request_buy/', include('request_buy.urls')),
    path('news/', include('news.urls')),

    # baton admin
    path('baton/', include('baton.urls')),


    # for home page
    path('others/', include('others.urls')),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
