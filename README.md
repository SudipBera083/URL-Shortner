# 🔗 URL Shortener

A sleek, modern, and responsive **URL Shortener Web Application** built with **Django** and a stunning **Glassmorphism UI**.  
It shortens long URLs into compact links, features a **genuine progress bar**, and provides a **copy-to-clipboard** button — making the experience seamless and interactive.

---

## 🌟 Features

- ✨ **Modern Glassmorphism UI**  
- ⚡ **Instant URL shortening**  
- 🧭 **Animated genuine progress bar**  
- 📋 **Copy short URL to clipboard**  
- 🛡️ **CSRF protected form** (for Django)  
- 📱 **Fully responsive layout**  
- 💜 **Made with HTML, CSS, JS, and Django**

---

## 🖼️ Preview

![URL Shortener Preview](https://github.com/SudipBera083//assets/preview-url-shortener.png)

---

## 🛠️ Tech Stack

| Layer | Technology |
|--------|-------------|
| Backend | Django (Python 3) |
| Frontend | HTML5, CSS3, JavaScript |
| Database | SQLite (default Django DB) |
| Deployment | Vercel / Render / Railway (optional) |

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git https://github.com/SudipBera083/URL-Shortner.git
cd url-shortener
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate     # (Mac/Linux)
venv\Scripts\activate        # (Windows)
```

### 3️⃣ Install Dependencies
```bash
pip install django
```

### 4️⃣ Run the Server
```bash
python manage.py runserver
```

Now open your browser and visit 👉 **http://127.0.0.1:8000/**

---

## 📂 Project Structure
```
url_shortener/
│
├── shortner/               # Main Django app
│   ├── templates/
│   │   └── home.html       # Beautiful frontend UI
│   ├── views.py            # Handles shortening logic
│   ├── models.py           # URL model
│   ├── urls.py             # App-level routing
│   └── admin.py
│
├── url_shortener/          # Project root
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

## 🧠 How It Works

1. User pastes a long URL in the input box.  
2. Progress bar starts and shows genuine animation.  
3. Django shortens the URL and returns a short version.  
4. User can copy the short link instantly.  

---

## 🧩 Example

**Input:**  
```
https://www.linkedin.com/in/sudipbera083/
```

**Output:**  
```
https://da.gd/N3hJ6
```

---

## 💡 Future Enhancements

- Add user login & history of shortened URLs  
- Analytics (click count, last accessed time)  
- QR Code generation for each short URL  
- API endpoint for external integrations  

---

## 💻 UI Snippet

```html
<div class="progress-bar" id="progressBar">
  <div class="progress" id="progress"></div>
</div>
```

```js
form.addEventListener('submit', () => {
  progressBar.style.display = 'block';
  progress.style.width = '0%';
  setTimeout(() => { progress.style.width = '100%'; }, 100);
  setTimeout(() => { progressBar.style.display = 'none'; }, 3000);
});
```

---

## 🧑‍💻 Author

**👤 [Sudip Bera](https://github.com/SudipBera083)**  
💼 Programmer Analyst Trainee @ Cognizant  
💬 Specialist in Oracle Cloud HCM, Django, and Python  
📫 Reach me: [LinkedIn](https://linkedin.com/in/sudipbera083)

---

## 🪪 License

This project is licensed under the **MIT License** — feel free to use and modify it as you like.

```
MIT License © 2025 Sudip Bera
```

---

> _“Turning long links into elegant short stories — one click at a time.”_
