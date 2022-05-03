from django.contrib import admin
from django.urls import path,include

from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "cla"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name='index' ),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
