from django.conf.urls import url,include
from . import views


urlpatterns = [

    url(r'^$', views.dte_list, name='dte_list'),
    url(r'^parser/$', views.frame, name='parser'),
    url(r'^personel/new/$', views.personel_new, name='personel_new'),
    url(r'^new/dte/$', views.new_dte, name='new_dte'),
    url(r'^work_list$', views.get_work, name='work_list'),
    url(r'^dtes/$', views.dte_list, name='dtes'),
    url(r'^dte/(?P<nn>[0-9]+)/edit/$', views.dte_edit, name='dte_edit'),
    url(r'^report/(?P<d>\w+)/(?P<m>\w+)/(?P<y>\w+)/$', views.report, name='make'),

    url(r'^contras/$', views.contras, name='contras'),
    url(r'^contra/new/$', views.contra_new, name='contra_new'),
    url(r'^contra/(?P<nn>[0-9]+)/edit/$', views.contra_edit, name='contra_edit'),

    url(r'^btss/$', views.btss, name='btss'),
    url(r'^bts/new/$', views.bts_new, name='bts_new'),
    url(r'^bts/(?P<nn>[0-9]+)/edit/$', views.bts_edit, name='bts_edit'),

    url(r'^cars/$', views.cars, name='cars'),
    url(r'^car/new/$', views.car_new, name='car_new'),
    url(r'^car/(?P<nn>[0-9]+)/edit/$', views.car_edit, name='car_edit'),

    url(r'^works/$', views.works, name='works'),
    url(r'^work/new/$', views.work_new, name='work_new'),
    url(r'^work/(?P<nn>[0-9]+)/edit/$', views.work_edit, name='work_edit'),



]

urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
]