# 🚀 SyncReserve AI

> **High-Performance Campus Resource Scheduling Engine**
> Built with **C++**, **Python**, **FastAPI**, and a modern web interface.

---

## 📌 Overview

SyncReserve AI is a high-performance scheduling system designed to manage campus resource bookings efficiently while preventing scheduling conflicts.

Unlike traditional reservation systems that rely heavily on database locking and expensive queries, SyncReserve AI leverages a **C++ graph-based scheduling engine** for fast validation and conflict detection.

The system is demonstrated through a modern web interface powered by FastAPI and JavaScript.

---

## ✨ Features

- ⚡ High-speed C++ Scheduling Engine
- 🔒 Conflict Detection
- 📚 Persistent Booking Journal
- 🌐 FastAPI REST API
- 🖥 Modern Interactive Frontend
- 📊 Live Backend Activity
- 🔄 Python-C++ Bridge
- 📈 Performance-focused Architecture

---

# 🏗 Architecture

```
                 User
                  │
                  ▼
        HTML / CSS / JavaScript
                  │
                  ▼
             FastAPI Backend
                  │
                  ▼
            Python Bridge Layer
                  │
                  ▼
       C++ Scheduling Engine
                  │
                  ▼
           JSON Response
                  │
                  ▼
             Frontend Update
```

---

# 📂 Project Structure

```
SyncReserve-AI/

│
├── backend/
│   ├── api/
│   ├── bridge/
│   ├── cpp/
│   ├── database/
│   └── ...
│
├── frontend/
│   ├── css/
│   ├── js/
│   └── index.html
│
└── README.md
```

---

# 🛠 Tech Stack

### Backend

- Python 3
- FastAPI
- Uvicorn

### Scheduling Engine

- C++17

### Frontend

- HTML5
- CSS3
- JavaScript

### Data Storage

- JSON Journal

---

# ⚙ Workflow

```
Booking Request

      │

      ▼

Frontend

      │

      ▼

FastAPI

      │

      ▼

Python Bridge

      │

      ▼

Journal Validation

      │

      ▼

C++ Scheduling Engine

      │

      ▼

Booking Accepted / Rejected

      │

      ▼

Journal Updated

      │

      ▼

Response Returned
```

---

# 🚀 Running the Project

## 1. Clone Repository

```bash
git clone https://github.com/tanu25bce10493/Team-GRAMBYTE-TANU_GOWDA.git
```

---

## 2. Backend

```bash
cd backend

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

python -m uvicorn api.main:app --reload
```

Backend runs on

```
http://127.0.0.1:8000
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## 3. Frontend

```bash
cd frontend

python -m http.server 5500
```

Open

```
http://localhost:5500
```

---

# 📋 API

## POST

```
/api/book
```

### Request

```json
{
    "student_id":"22BCE0001",
    "resource_id":"LAB-101",
    "start_time":"2026-08-01T10:00:00",
    "end_time":"2026-08-01T11:00:00"
}
```

---

### Response

```json
{
    "success": true,
    "status": 200,
    "message": "Booking confirmed"
}
```

---

# 📁 Journal Storage

Bookings are stored in

```
backend/database/journal.json
```

Example

```json
[
    {
        "resource_id":"LAB-101",
        "start_time":"2026-08-01T10:00:00",
        "end_time":"2026-08-01T11:00:00",
        "timestamp":"2026-08-01T09:55:12"
    }
]
```

---

# 📸 Screenshots

- Homepage
- <img width="1280" height="798" alt="Screenshot 2026-07-31 111039" src="https://github.com/user-attachments/assets/39699e19-958d-499f-a86a-e93f8adc1c3d" />

- Booking Dashboard
- <img width="1280" height="800" alt="Screenshot 2026-07-31 111203" src="https://github.com/user-attachments/assets/1dcdf9d4-1603-4677-93a2-4d223838d19a" />

- Live Pipeline
- <img width="1280" height="800" alt="Screenshot 2026-07-31 111146" src="https://github.com/user-attachments/assets/c88fd972-07af-4098-974f-55a5741021c6" />

- Backend Terminal
- <img width="1280" height="800" alt="Screenshot 2026-07-31 111224" src="https://github.com/user-attachments/assets/62339671-4a0e-4e03-b6b2-de8916dfe833" />


---

# 🎯 Future Improvements

- AI-powered resource recommendation
- Persistent C++ scheduling service
- PostgreSQL support
- Authentication
- Admin dashboard
- Analytics
- Real-time WebSocket updates

---

# 👥 Team

**GRAMBYTE**

Summer of CodeFest

---

# 📜 License

This project is developed for educational and hackathon purposes.
