from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

def index(request):
    return render(request, 'packer/index.html')

