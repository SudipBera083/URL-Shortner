# 🔗 URL Shortener + QR Generator API

A sleek, modern, and responsive **URL Shortener Web Application** built with **Django REST Framework**, featuring a **Glassmorphism UI**, **genuine progress bar**, and **QR code generation** for each shortened link.

---

## 🌟 Features

- ✨ **Modern Glassmorphism UI**
- ⚡ **Instant URL shortening**
- 🧭 **Animated genuine progress bar**
- 📋 **Copy-to-clipboard functionality**
- 🧾 **Generate QR Code for any URL**
- 🛡️ **CSRF protected form**
- 📱 **Fully responsive layout**
- 💜 **Built using Django, HTML, CSS, and JS**

---


## 🖼️ Preview

![URL Shortener Preview](https://github.com/SudipBera083/URL-Shortner/blob/main/assets/preview.png)

---

## 🛠️ Tech Stack

| Layer | Technology |
|--------|-------------|
| Backend | Django + Django REST Framework |
| Frontend | HTML5, CSS3, JavaScript |
| Database | SQLite3 |
| Language | Python 3.11+ |
| Deployment | Vercel / Render / Railway (optional) |

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/SudipBera083/URL-Shortner.git
cd URL-Shortner
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate # macOS/Linux
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Server
```bash
python manage.py runserver
```

Now visit 👉 **http://127.0.0.1:8000/**  
You’ll see the stunning UI for URL shortening and QR generation.

---

## 📡 API Endpoints

| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/api/shorten/` | **POST** | Shortens a given long URL |
| `/api/generate-qr/` | **POST** | Generates a QR Code for a given URL |
| `/api/shorten/<short_code>/` | **GET** | Redirects to the original URL (if implemented) |

---

## 📬 Example Requests

### ✅ 1. Shorten a URL

**Endpoint:**  
`POST http://127.0.0.1:8000/api/shorten/`

**Request Body (JSON):**
```json
{
  "original_url": "https://www.linkedin.com/in/sudipbera083/"
}
```

**Response:**
```json
{
  "original_url": "https://www.linkedin.com/in/sudipbera083/",
  "short_url": "https://da.gd/XyZ123"
}
```

---

### ✅ 2. Generate a QR Code

**Endpoint:**  
`POST http://127.0.0.1:8000/api/generate-qr/`

**Request Body (JSON):**
```json
{
  "url": "https://da.gd/XyZ123"
}
```

**Response:**
```json
{
  "qr_code": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA..."
}
```

💡 _The returned Base64 image can be directly embedded in an `<img>` tag on your frontend._

---

## 🧭 Using Postman

1. **Open Postman**
2. Create a new **POST** request to `http://127.0.0.1:8000/api/shorten/`
3. Go to **Body → raw → JSON**
4. Paste:
   ```json
   {
     "original_url": "https://github.com/SudipBera083"
   }
   ```
5. Click **Send**  
   ✅ You’ll receive the shortened URL as response.

For QR:
```json
{
  "url": "https://da.gd/XyZ123"
}
```

---

## 📂 Project Structure

```
url_shortener/
│
├── shortner/
│   ├── templates/
│   │   └── home.html         # Beautiful frontend UI
│   ├── views.py              # URL & QR logic
│   ├── urls.py               # API endpoints
│   ├── serializers.py        # REST serializers
│   └── models.py             # Optional: save short URLs
│
├── url_shortener/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── requirements.txt
├── manage.py
└── README.md
```

---

## 🧩 How It Works

1. User pastes a long URL in the input box.
2. The genuine progress bar animates while processing.
3. Django REST shortens the URL.
4. Optionally, a QR code is generated for instant sharing.
5. User copies or downloads the result.

---

## 💡 Future Enhancements

- ✅ Click tracking and analytics  
- ✅ User login and URL history  
- ✅ Expiration time for short links  
- ✅ Downloadable QR codes  
- ✅ API key-based access

---

## 🧑‍💻 Author

**👤 [Sudip Bera](https://github.com/SudipBera083)**  
💼 Programmer Analyst @ Cognizant  
💬 Specialist in **Oracle Cloud HCM**, **Django**, and **Python**  
📫 [LinkedIn](https://linkedin.com/in/sudipbera083)

---

## 🪪 License

This project is licensed under the **MIT License**.

```
MIT License © 2025 Sudip Bera
```

---

> _“Turning long links into elegant short stories — and now, QR-powered too.”_
