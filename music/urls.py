from django.conf.urls import patterns,include,url
from . import views

#urlpatterns = patterns('',url(r'^',ListView.as_view(queryset=Post.objects.all()order_by"-date")[:10],template_name="blog.html")),)

urlpatterns = [
    url(r'^$', views.SpecificSong, name='SpecificSong'),
]