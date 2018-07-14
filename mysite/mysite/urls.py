from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')), #(path(route, view))
    path('admin/', admin.site.urls),
]