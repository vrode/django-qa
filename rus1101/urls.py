from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

module = __name__.replace( ".urls", "" ) + ".";

urlpatterns = patterns('',
    url(r'^$',          module + 'views.index',           name="index" ),
    url(r'^add/$',      module + 'views.home',            name="home" ),
    url(r'^save/$',     module + 'views.save',            name="save" ),
    url(r'^random/$',   module + 'views.random',          name="random" ),
    url(r'^list/$',     module + 'views.list',            name="list" ),
);