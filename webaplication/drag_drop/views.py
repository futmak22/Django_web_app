from django.http import HttpResponseRedirect 
from django.shortcuts import render
from .forms import UploadFileForm
from .processfiles import handle_uploaded_file #Function for file process
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return render(request, 'drag_drop/drag_drop_index.html' , {})


def upload_file(request):
    #if request.method == 'POST' and request.FILES['myfile']:
    #    myfile = request.FILES['myfile']
    #    fs = FileSystemStorage()
    #    filename = fs.save(myfile.name, myfile)
    #    uploaded_file_url = fs.url(filename)
    #    return render(request, 'drag_drop/loadfileform.html', { 'uploaded_file_url': uploaded_file_url })
    print("Impresion desde Upload_files. Super!!!")
    return render(request, 'drag_drop/loadfileform.html')

