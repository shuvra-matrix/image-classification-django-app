from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.


def index(request):
    if request.method == "POST":
        file = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)
        mydict = {
            'img' :uploaded_file_url,
        }
        return render(request, 'index.html', context=mydict)
    return render(request, 'index.html')
