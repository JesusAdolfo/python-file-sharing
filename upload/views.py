from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Upload
from django.views.static import serve
import os
from django.http import HttpResponse
from django.utils.encoding import smart_str
from wsgiref.util import FileWrapper
import uuid
from django.core.files import File


class IndexView(generic.ListView):
    template_name = 'upload/index.html'

    def get_queryset(self):
        return Upload.objects.all()


class DetailView(generic.DetailView):
    model = Upload
    template_name = 'upload/detail.html'


class FileCreate(CreateView):
    model = Upload
    fields = ['name', 'file']


class SuccessView(generic.TemplateView):
    template_name = 'upload/sucess.html'


def download(request, upload_id):
    my_file = Upload.objects.get(pk=upload_id)
    print("test==", my_file.file)
    filename = my_file.file
    path = "media/" + str(my_file.file)
    print("test2: ", path)
    print("test3: ", path.split('.').pop())

    # return serve(request, os.path.basename(path), os.path.dirname(path))
    filename = path # Select your file here.
    wrapper = FileWrapper(open(filename, 'rb'))
    response = HttpResponse(wrapper, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="test.jpg"'
    response['Content-Length'] = os.path.getsize(filename)
    return response