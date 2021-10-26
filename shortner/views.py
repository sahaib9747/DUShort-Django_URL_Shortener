import uuid
import json 

from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import URLShortner

# Create your views here.
def index(request):
    return render(request, 'index.html')


def short(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data = json.loads(data)
        data = data['link']

        url = URLShortner.objects.filter(link=data)
        root_url = 'http://127.0.0.1:8000/'
        if url.exists():
            return HttpResponse(root_url + url[0].uuid)
        else:
            uid = str(uuid.uuid4())[:5]
            url = URLShortner.objects.create(link=data, uuid=uid)
            url.save()
            print(url.uuid)
            return HttpResponse(root_url + url.uuid)
        
def go(reqeust, link):
    url = URLShortner.objects.get(uuid=link).link
    print(url)
    return redirect(url)