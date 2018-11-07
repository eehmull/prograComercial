from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.listar, name= 'listar'),
        #url(r'^$', views.login, name= 'login'),
        url(r'^detalle/(?P<pk>[0-9]+)/$', views.detalle, name='detalle'),
        url(r'^publicacion/nueva/$', views.nuevo, name='nuevo'),
        url(r'^publicacion/(?P<pk>[0-9]+)/editar/$', views.editar, name='editar'),
        url(r'^borrador/$', views.borrador, name='borrador'),
        url(r'^publicacion/(?P<pk>\d+)/publicarborrador/$', views.publicarborrador, name='publicarborrador'),
        url(r'^publicacion/(?P<pk>\d+)/remover/$', views.remover, name='remover'),
]
