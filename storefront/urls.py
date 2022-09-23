from django.contrib import admin
from django.urls import path, include
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('playground.urls', namespace='playground')),
    path('__debug__/', include(debug_toolbar.urls)),
]
