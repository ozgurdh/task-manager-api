# Task Manager REST API

A simple RESTful API built with FastAPI for managing tasks. This project demonstrates backend development fundamentals including CRUD operations, database integration, and containerization.

---

## 🚀 Features

- Create, read, update and delete tasks (CRUD)
- SQLite database integration using SQLModel
- Clean and modular project structure (main, schemas, crud)
- RESTful API design
- Docker support

---

## 🛠️ Tech Stack

- Python
- FastAPI
- SQLModel
- SQLite
- Docker

---

## 📂 Project Structure

task-manager-api/
│
├── app/
│ ├── main.py # API endpoints
│ ├── database.py # DB connection
│ ├── models.py # Database models
│ ├── schemas.py # Request/response models
│ └── crud.py # Database operations
│
├── Dockerfile
├── requirements.txt
└── README.md

---

## ▶️ Run Locally (Optional)

**1. Clone the Repository:**
```bash
git clone <your-repo-link>
cd task-manager-api
```

**2. Create a virtual environment:**
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Run the application:**
```bash
uvicorn app.main:app --reload
```

**API will be available at:**
```bash
http://127.0.0.1:8000/docs
```

---

## 🐳 Run with Docker (Recommended)

**1. Clone the Repository:**
```bash
git clone <your-repo-link>
cd task-manager-api
```

**2. Build the Docker image:**
```bash
docker build -t task-api .
```

**3. Run the container:**
```bash
docker run -p 8000:8000 task-api
```

**4. Open the API documentation:**
```bash
http://localhost:8000/docs
```

---

## 📬 Example Request

```bash
{
  "id": 10,
  "title": "Learn FastAPI",
  "description": "Build a REST API project",
  "completed": false
}
```
