from django.conf.urls import url
from . import views

app_name = 'upload'

urlpatterns = [

    # /upload/
    url(r'^$', views.index, name='index'),

    # /upload/43/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /upload/43/favorite
    url(r'^(?P<upload_id>[0-9]+)/downloaded/$', views.downloaded, name='downloaded'),


    #upload/add
    url(r'add/$', views.FileCreate.as_view(), name='file-add'),

]
