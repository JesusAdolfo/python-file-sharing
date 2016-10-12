from django.conf.urls import url
from . import views

app_name = 'upload'

urlpatterns = [

    # /upload/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /upload/43/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #upload/add
    url(r'add/$', views.FileCreate.as_view(), name='file-add'),

    #upload/success
    url(r'sucess/$', views.SuccessView.as_view(), name='success'),

    #upload/files
    url(r'files/$', views.FilesView.as_view(), name='files'),

    url(r'^downloads/(?P<upload_id>[0-9]+)/$', views.download, name='download'),

]
