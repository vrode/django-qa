from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns( '',
    url( r'^$',          'alpha.views.index',           name="index" ),
    url( r'^add/$',      'alpha.views.home',            name="home" ),
    url( r'^save/$',     'alpha.views.save',            name="save" ),
    url( r'^random/$',   'alpha.views.random',          name="random" ),
    url( r'^list/$',     'alpha.views.list',            name="list" ),
);