from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from NetworkLink import views

import os



urlpatterns = [
    # Examples:
    url(r'fire', views.fire, name='fire'),
    # url(r'update', 'NetworkLink.views.update', name='update'),
    # (r'^kml/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
    url(r'welcome', views.welcome, name='welcome'),
    # url(r'welcome', 'NetworkLink.views.gather', name='gather'),




    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


