from django.shortcuts import render
import pyshorteners
import qrcode
import io
import base64
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def home(request):
    return render(request, 'home.html')

def url_shortened(request):
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        s = pyshorteners.Shortener()
        short_url = s.dagd.short(original_url)

        # Generate QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(short_url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Convert QR to base64
        buffer = io.BytesIO()
        img.save(buffer, format='PNG')
        qr_image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

        return render(
            request,
            'home.html',
            {
                'short_url': short_url,
                'original_url': original_url,
                'qr_image': qr_image_base64,
            }
        )
    return render(request, 'home.html')



@api_view(['POST'])
def shorten_url(request):
    """
    POST /api/shorten/
    Body: { "url": "https://example.com" }
    """
    original_url = request.data.get('url')
    if not original_url:
        return Response({"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        s = pyshorteners.Shortener()
        short_url = s.dagd.short(original_url)
        return Response({"original_url": original_url, "short_url": short_url}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def generate_qr(request):
    """
    POST /api/generate-qr/
    Body: { "url": "https://short.url/abc" }
    """
    url = request.data.get('url')
    if not url:
        return Response({"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')

        buffer = io.BytesIO()
        img.save(buffer, format='PNG')
        img_str = base64.b64encode(buffer.getvalue()).decode()
        qr_data = f"data:image/png;base64,{img_str}"

        return Response({"url": url, "qr_image": qr_data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
