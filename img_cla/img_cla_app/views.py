from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from keras.preprocessing import image
import numpy as np
from keras.models import load_model
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.


def index(request):
    
    if request.method == "POST":
        if request.session.has_key('uploaded_file'):
            file_urls = request.session.get('uploaded_file')
            os.remove(f"./{file_urls}")
            del request.session['uploaded_file']
            
        prediction = ""
        file = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        request.session['uploaded_file'] = fs.url(filename)
        file_urls = request.session.get('uploaded_file')
     
        model = load_model('./saved_model/CNN_Cat_Dog_Model.h5')
        model.summary()
        model.weights
        model.optimizer
        test_image = image.load_img(f"./{file_urls}", target_size=(64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = model.predict(test_image)
        if result[0][0] == 1:
            prediction = 'DOG'
        else:
            prediction = 'CAT'
            
        mydict = {
            'img': file_urls,
            'pre': prediction,
        }
    
        return render(request, 'index.html', context=mydict)
    return render(request, 'index.html')
