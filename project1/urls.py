from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('Productores/', include('Productores.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
