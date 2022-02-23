from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import Home.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('home/', include('Home.urls', namespace='shop')),
    path('index', Home.views.index),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
