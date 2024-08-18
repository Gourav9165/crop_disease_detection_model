from django import forms
from .models import UploadedImage

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image']

class ImageURLForm(forms.Form):
    image_url = forms.URLField(label='Enter URL of Image', max_length=200)
