import base64
import io

from django.shortcuts import render

def index(request):
    return render(request, 'demo/index.html')

def pill_recognise(request):
    context = {}
    if request.POST:
        context["image"] = True

        context["image_extension"] = request.FILES["image"].name[-3:]
        
        request_image_io = io.BytesIO(request.FILES["image"].read())
        context["image_str"] = base64.b64encode(request_image_io.read()).decode('utf-8')

    return render(request, 'demo/recognise.html', context)
