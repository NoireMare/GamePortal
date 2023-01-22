from django.contrib import admin
from django.urls import path, include
from blog.views import IndexView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='home_page'),
    path('blog/', include('blog.urls')),
    path('users/', include('users.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
