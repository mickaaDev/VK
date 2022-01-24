from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("core.urls")),
    path('', include("message.urls")),
    path('friendship/', include('friendship.urls')),
    # path('accounts/', include('allauth.urls')),
    path('', include('publications.urls')),
    path('feedback/',include('feedback.urls')),
    path('gallery/',include('gallery.urls'))
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

