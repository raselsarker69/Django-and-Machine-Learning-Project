from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('predict/', views.predict, name='prediction'),
    path('predict/result/', views.result, name='result')
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)