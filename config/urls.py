from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from config import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),


] + i18n_patterns(
    path('i18n', include('django.conf.urls.i18n')),
    path('api/v1/', include('posts.urls')),
    path('api/v1/', include('contact.urls')),
    path('', include('home_app.urls')),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


schema_view = get_schema_view(
   openapi.Info(
      title="Dream Team API",
      default_version='v1',
      description="Dream Team",
      terms_of_service="dream_team.com",
      contact=openapi.Contact(email="sunnatakbarov028@gmail.com"),
      license=openapi.License(name="DT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny,],
)

urlpatterns += [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('docs/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('docs/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
