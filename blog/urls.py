from django.conf.urls import patterns,include,url
from . import views

#urlpatterns = patterns('',url(r'^',ListView.as_view(queryset=Post.objects.all()order_by"-date")[:10],template_name="blog.html")),)

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]