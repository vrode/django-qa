from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qa.views.home', name='home'),
    # url(r'^qa/', include('qa.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$',          'alpha.views.home',     name="home" ),
    url(r'^save/$',     'alpha.views.save',     name="save" ),
    url(r'^random/$',   'alpha.views.random',   name="random" ),
    url(r'^list/$',     'alpha.views.list',     name="list" ),
    # url(r'^inf1080/$',  'inf1080.views.', name="random" ),
    # url(r'^inf1010/$',  'inf1010.views.', name="random" ),
    # url(r'^rus1101/$',  'rus1101.views.', name="random" ),
    # url(r'^rus1102/$',  'rus1102.views.', name="random" ),
)
