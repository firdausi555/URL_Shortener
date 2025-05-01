from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
from django.http import HttpResponse

def home(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        url = URL.objects.create(original_url=original_url)
        return render(request, 'shortener/success.html', {'short_code': url.short_code})
    return render(request, 'shortener/home.html')

def redirect_url(request, short_code):
    url = get_object_or_404(URL, short_code=short_code)
    return redirect(url.original_url)
