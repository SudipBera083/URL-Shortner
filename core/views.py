from django.shortcuts import render
import pyshorteners

def home(request):
    short_url = None
    original_url = None

    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        if original_url:
            try:
                s = pyshorteners.Shortener()
                short_url = s.dagd.short(original_url)
            except Exception as e:
                short_url = f"Error: {str(e)}"

    return render(request, 'home.html', {'short_url': short_url, 'original_url': original_url})
