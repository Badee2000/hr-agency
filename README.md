# 💼 Django HR Agency Platform

A web-based platform built with **Django**, designed for HR agencies to manage operations, user roles, and intelligent communication in one place.

---

## ✨ Features

✅ **Django Admin Panel**  
- Manage users, companies, and candidates through a robust admin interface.
- Permissions control who can access different data and features.

---

✅ **Real-Time Chat System (Long Polling)**  
- Integrated chat feature supporting:
  - Sending and receiving messages in near real-time.
  - Selecting who can participate in each chat conversation.

> **About Long Polling:**  
> Long polling is a technique that allows real-time updates without using WebSockets. Instead of constantly sending rapid requests, the client sends one request and waits until the server has new data to return. Once a message arrives, the server responds, and the client immediately sends a new request, achieving real-time communication while keeping the implementation simpler.

---

✅ **AI Chat Assistant via OpenRouter API**  
- Users with admin panel permissions can interact with an AI chatbot.
- The chatbot is trained on a **knowledge base** relevant to the HR domain.
- Use cases include:
  - Helping HR staff answer questions.
  - Automating candidate conversations.
  - Providing instant insights for companies.

---

✅ **Flexible User Roles**

Your application supports these roles:

| Role                  | Description                                                |
|------------------------|------------------------------------------------------------|
| **Superuser**         | Full access and management capabilities.                   |
| **HR Agency Employee**| Agency staff managing candidates and companies.            |
| **Company**           | Represents a company entity using the agency services.     |
| **Company Employee**  | Employees belonging to a specific company.                 |
| **Candidate**         | Individuals seeking jobs through the HR agency.            |

---

✅ **Proxy User Models**

- All user types extend the Django `auth.User` model using **proxy models**:
  - Candidate
  - Agency Employee
  - Company Employee

This approach allows:
- Managing all users under a single **Accounts** section.
- Displaying both shared user fields (username, email, etc.) and role-specific details (e.g. candidate profile info) in the admin panel.

---

✅ **Login with Username or Email**

- Users can log in with either their **username or email address** for greater convenience.

---

## 🛠️ Tech Stack

- Django (backend and admin)
- HTML / CSS / JS (frontend templates and chat interface)
- Long polling for real-time chat
- OpenRouter API for AI integration
- Python 3.10+
- SQLite (default, can switch to PostgreSQL)

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
````

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Set Up Environment Variables

Create a `.env` file in your project root:

```
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
OPENROUTER_API_KEY=your_openrouter_api_key
```

---

### 5. Apply Migrations

```bash
python manage.py migrate
```

---

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

---

### 7. Run the Development Server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access your app.

---

## 🔐 Environment Variables

| Variable             | Purpose                            |
| -------------------- | ---------------------------------- |
| `SECRET_KEY`         | Django secret key                  |
| `DEBUG`              | Debug mode (True/False)            |
| `DATABASE_URL`       | Database connection URL            |
| `OPENROUTER_API_KEY` | API key for OpenRouter integration |

---

## 💬 How It Works

* **Admin Panel** → Manage users, companies, candidates, and chat conversations.
* **Long Polling Chat**:

  * Client sends a request and waits for new messages.
  * Server responds when new data is available.
* **AI Chat**:

  * Authorized users can chat with the AI trained on a specialized HR knowledge base.
  * Integrated using the OpenRouter API.

---

## 🤝 Contributing

Pull requests are welcome! For significant changes, open an issue first to discuss your ideas.

---

## 📝 License

[MIT](LICENSE)

---

## 📣 Acknowledgments

* Django Community
* OpenRouter API

---

```

---

### ✅ How to Use This README

- Save the entire text above as `README.md` in your project root.
- Replace:
  - `https://github.com/yourusername/yourrepo.git` → your real repo URL.
  - API keys and any private details.
- Optionally add:
  - Screenshots
  - Deployment instructions
  - Badges (GitHub Actions, coverage, etc.)

Let me know if you’d like:

- Shorter or more concise wording?
- More technical depth (e.g. API usage examples)?
- Screenshots or diagrams added?
```
