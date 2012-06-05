from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

def relative_url( pattern, view ):
    return url( pattern, "%s.%s" % (__package__, view) ) ;

urlpatterns = patterns('',
    relative_url( r'^$',          'views.index' ),
    relative_url( r'^add/$',      'views.home' ),
    relative_url( r'^save/$',     'views.save' ),
    relative_url( r'^random/$',   'views.random' ),
    relative_url( r'^list/$',     'views.list' ),
);