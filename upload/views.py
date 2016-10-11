from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Upload


def index(request):
    all_files = Upload.objects.all()
    context = {
        'all_files': all_files,
    }
    return render(request, 'upload/index.html', context)


class DetailView(generic.DetailView):
    model = Upload
    template_name = 'upload/detail.html'


def downloaded(request):
    all_files = Upload.objects.all()
    try:
        selected_file = request.POST['file']
    except(KeyError, Upload.DoesNotExist):
        return render(request, 'index.html', {
            'all_files': all_files,
            'error_message': "You did not select a valid file"
        })
    else:
        selected_file.downloaded = True
        selected_file.save()
        return render(request, 'upload/index.html', {'all_files': all_files})


class FileCreate(CreateView):
    model = Upload
    fields = ['name', 'file']