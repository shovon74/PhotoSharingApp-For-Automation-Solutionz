from django.conf.urls import url
from . import views

app_name = 'photo'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<image_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^images/(?P<filter_by>[a-zA_Z]+)/$', views.images, name='images'),
    url(r'^create_album/$', views.create_album, name='create_album'),
    url(r'^(?P<album_id>[0-9]+)/create_image/$', views.create_image, name='create_image'),
    url(r'^(?P<album_id>[0-9]+)/delete_image/(?P<image_id>[0-9]+)/$', views.delete_image, name='delete_image'),
    url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),
]
