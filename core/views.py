from django.shortcuts import render
import pyshorteners
import qrcode
import io
import base64

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
