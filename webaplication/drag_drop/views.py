from django.http import HttpResponseRedirect 
from django.shortcuts import render
from .forms import UploadFileForm
from .processfiles import handle_uploaded_file #Function for file process
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'drag_drop/drag_drop_index.html' , {})


def upload_file(request):
    if request.method == 'POST' and request.FILES['First_File']:
        print(request.FILES)
        myfile = request.FILES['First_File']
        print("Nombre del archivo cargado: {}".format(myfile.name))
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        
        messages.success(request, 'El archivo fue cargado en la ruta: drag_drop/media{}'.format(uploaded_file_url))
        return render(request, 'drag_drop/loadfileform.html', { 'uploaded_file_url': uploaded_file_url })
    
    return render(request, 'drag_drop/loadfileform.html')

