from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import UploadedImage
import tensorflow as tf
from PIL import Image, ImageOps, UnidentifiedImageError
import numpy as np
import requests
from io import BytesIO
from .forms import ImageUploadForm, ImageURLForm

# Load the TFLite model
model_path = "detection/model.tflite"
labels_path = "detection/labels.txt"
interpreter = tf.lite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

# Load class names
with open(labels_path, "r") as file:
    class_names = [line.strip() for line in file.readlines()]

def home(request):
    return render(request, 'detection/upload.html')

def weather_view(request):
    return render(request, 'detection/weather.html')

def upload_image(request):
    if request.method == 'POST':
        upload_form = ImageUploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            upload_form.save()
            uploaded_image = upload_form.instance
            result = predict_image(uploaded_image.image.path)
            if 'error' in result:
                return render(request, 'detection/upload_image.html', {
                    'upload_form': upload_form,
                    'error': result['error']
                })
            else:
                return render(request, 'detection/result.html', {
                    'class_name': result['class_name'],
                    'confidence': result['confidence'],
                    'image_url': uploaded_image.image.url
                })
        else:
            return render(request, 'detection/upload_image.html', {
                'upload_form': upload_form,
                'error': 'Invalid form submission. Please try again.'
            })
    else:
        upload_form = ImageUploadForm()

    return render(request, 'detection/upload_image.html', {
        'upload_form': upload_form,
    })


def enter_url(request):
    if request.method == 'POST':
        url_form = ImageURLForm(request.POST)
        if url_form.is_valid():
            image_url = url_form.cleaned_data['image_url']
            result = predict_image(image_url)
            if 'error' in result:
                return render(request, 'detection/enter_url.html', {
                    'url_form': url_form,
                    'error': result['error']
                })
            else:
                return render(request, 'detection/result.html', {
                    'class_name': result['class_name'],
                    'confidence': result['confidence'],
                    'image_url': image_url
                })
    else:
        url_form = ImageURLForm()

    return render(request, 'detection/enter_url.html', {
        'url_form': url_form,
    })

def predict_image(image_path_or_url):
    try:
        if image_path_or_url.startswith('http'):
            # Handle the image as a URL
            response = requests.get(image_path_or_url)
            image = Image.open(BytesIO(response.content)).convert("RGB")
        else:
            # Handle the image as a file path
            image = Image.open(image_path_or_url).convert("RGB")

        # Resize the image and normalize
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

        # Set the tensor to point to the input data
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()
        interpreter.set_tensor(input_details[0]['index'], [normalized_image_array])

        # Run the model
        interpreter.invoke()

        # Get the output tensor
        output_data = interpreter.get_tensor(output_details[0]['index'])

        # Get the predicted class and confidence score
        index = np.argmax(output_data)
        class_name = class_names[index]
        confidence_score = output_data[0][index] * 100  # Convert to percentage

        return {'class_name': class_name, 'confidence': confidence_score}
    
    except (requests.exceptions.RequestException, UnidentifiedImageError, IOError) as e:
        # Return an error message if there was an issue with the URL or image
        return {'error': 'Invalid image or URL. Please try again with a different image or URL.'}
