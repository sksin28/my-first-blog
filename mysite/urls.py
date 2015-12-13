from django.conf.urls import include, url, patterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^music/', include('music.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
