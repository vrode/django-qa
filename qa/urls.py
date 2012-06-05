from django.conf.urls import patterns, include, url;

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
    
    url( r'',            include('alpha.urls') ),
    url( r'^inf1820/',   include('inf1820.urls') ),
    url( r'^rus1101/',   include('rus1101.urls') ),
    # url(r'^inf1010/$',  include('inf1010.urls') ),
    # url(r'^rus1102/$',  include('inf1102.urls') ),
);

