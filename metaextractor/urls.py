from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'extract.views.fetchView', name='home'),
    #url(r'^fetch/$', 'extract.views.fetchView', name='fetch'),
    url(r'^store/$', 'extract.views.storeView', name='store'),
    url(r'^done/$', 'extract.views.doneView', name='done'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
