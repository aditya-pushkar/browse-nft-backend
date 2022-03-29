from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v0/nft/', include('nft.urls')),
    path('api/v0/user/', include('user.urls')),
    path('api/v0/panel/', include('staff_panel.urls')),
]
