from django.urls import path
from django.conf.urls import url
from . import views
from .views import GeneratePdf

urlpatterns = \
    [path('', views.detail, name='main'),

	url(r'^edit', views.edit, name='edit'),

    url(r'^detail', views.detail, name='detail'),

    url(r'^login/$', views.login_user, name='login_user'),

    url(r'^pdf/$', GeneratePdf.as_view(), name='pdf'),
    ]