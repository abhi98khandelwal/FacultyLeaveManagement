"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^approve$',app.views.approveleave),
    url(r'^pendingleaves$',app.views.pendingleave,name = 'pendingleave'),
    url(r'^previousleaves$',app.views.previousleave,name = "previousleave"),
    url(r'^layout',app.views.layout),
    url(r'^index$',app.views.home,name = 'index'),
    url(r"^logout$",app.views.logout_view,name = 'logout'),
    # Examples:
    url(r'^$', app.views.login_view, name='login'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^applyleave$',app.views.applyleave, name = 'applyleave'),


    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
