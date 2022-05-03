from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from keras.preprocessing import image
import numpy as np
from keras.models import load_model
# Create your views here.


def index(request):
    
    if request.method == "POST":
        prediction = ""
        file = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)
        model = load_model('./saved_model/CNN_Cat_Dog_Model.h5')
        model.summary()
        model.weights
        model.optimizer
        test_image = image.load_img(f"./{uploaded_file_url}", target_size=(64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = model.predict(test_image)
        if result[0][0] == 1:
            prediction = 'dog'
        else:
            prediction = 'cat'
            
        mydict = {
            'img' :uploaded_file_url,
            'pre': prediction,
        }
    
        return render(request, 'index.html', context=mydict)
    return render(request, 'index.html')
