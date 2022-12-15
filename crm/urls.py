from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="APIs for CRM System",
      description='',
      default_version='v1',
      contact=openapi.Contact(email="abdunazarovdior@gmail.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

    
urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

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
