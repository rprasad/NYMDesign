from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from nymdesign.portfolio import views as portfolio_views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Example:
    # (r'^nymdesign/', include('nymdesign.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^portfolio/', include('nymdesign.portfolio.urls')),

    url(r'^info/', include('nymdesign.info_pages.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^nym-admin', include(admin.site.urls)),
    url(r'^admin-site/', include(admin.site.urls)),

    url(r'^$', portfolio_views.view_homepage, name='home'),

]
