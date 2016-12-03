from django.conf.urls import url
from django.contrib import admin
from final import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^language/$', views.language, name='language'),
    url(r'^similarity/$', views.similarity, name='similarity'),
    url(r'^encoding/$', views.encoding, name='encoding'),
    url(r'^decoding/$', views.decoding, name='decoding'),
    url(r'^natural/$', views.natural, name='natural'),
    url(r'^report/$', views.report, name='report'),
    url(r'^test_report/$', views.test_report, name='test_report'),
]
