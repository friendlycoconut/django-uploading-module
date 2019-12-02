
# social_app/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.login, name='login'),
    path('admin/', admin.site.urls),    
    path("login/", views.login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social")),

    path("upload/", views.upload, name="upload"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)