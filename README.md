# BITStruq — Developer Vault & Sandbox

A full-stack developer preparation workspace designed to bring programming practice, SQL experimentation, DSA resources, AI assistance, and campus placement experiences into one platform.

![Python](https://img.shields.io/badge/Python-3776AB?logo=python\&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi\&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript\&logoColor=black)
![React](https://img.shields.io/badge/React-20232A?logo=react\&logoColor=61DAFB)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql\&logoColor=white)

---

## 🚀 Live Demo

[Visit BITStruq](https://bitstruq.netlify.app/)

---

## 📸 Screenshots

### Home

![BITStruq Home](screenshots/home.png)

### SQL Sandbox

![SQL Sandbox](screenshots/sql-sandbox.png)

### Algorithm Vault

![Algorithm Vault](screenshots/algo-vault.png)

### Code Playground

![Code Playground](screenshots/code-playground.png)

### Campus Exchange

![Campus Exchange](screenshots/campus-exchange.png)

---

## ✨ Features

* 🤖 **AI Programming Assistant** — Get programming guidance and code suggestions using the Gemini API.
* 🗄️ **SQL Sandbox** — Write and execute SQL queries directly in the browser.
* 🧠 **Algorithm Vault** — Explore programming and algorithm concepts with examples and code snippets.
* 💻 **Multi-Language Code Playground** — Write and execute code in Python, C, C++, and Java.
* ⚡ **Remote Code Execution** — Execute submitted code through the Judge0 API.
* 🎓 **Campus Exchange** — Share and explore placement and internship experiences.
* ☁️ **Cloud Database Integration** — Store snippets and campus experiences using PostgreSQL/Supabase.
* 💾 **Local SQL History** — Preserve SQL query history locally for convenient experimentation.
* 📱 **Responsive Interface** — Access the workspace across different screen sizes.

---

## 🛠️ Tech Stack

### Frontend

* HTML
* JavaScript
* React
* Tailwind CSS
* AlaSQL

### Backend

* Python
* FastAPI
* Uvicorn
* Requests

### Database

* PostgreSQL
* Supabase

### APIs & Services

* Google Gemini API
* Judge0 API

---

## 🏗️ Architecture

```text
                         BITStruq
                            │
                            ▼
                  Frontend Application
                 (React + JavaScript)
                            │
                            │ HTTP Requests
                            ▼
                     FastAPI Backend
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ▼              ▼              ▼
        Gemini API      Judge0 API    PostgreSQL
                                        / Supabase
```

---

## 🔄 How It Works

### 🤖 AI Assistant

The frontend sends a user's programming question to the FastAPI backend. The backend communicates with the Gemini API and returns the generated response to the frontend.

### 💻 Code Playground

Users can select Python, C, C++, or Java, write source code, provide standard input, and execute the code. The backend sends the submission to Judge0 and returns the execution result.

### 🧠 Algorithm Vault

The Algorithm Vault provides a dedicated workspace for storing and accessing programming and algorithm-related snippets.

### 🗄️ SQL Sandbox

Users can experiment with SQL queries directly in the browser. SQL history is maintained locally for convenient access to previous queries.

### 🎓 Campus Exchange

Students can browse, search, and submit placement and internship experiences through the FastAPI backend and PostgreSQL database.

---

## 📁 Project Structure

```text
BITStruq/
│
├── frontend/
│   └── index.html
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── .env.example
│
├── screenshots/
│   ├── home.png
│   ├── sql-sandbox.png
│   ├── algo-vault.png
│   ├── code-playground.png
│   └── campus-exchange.png
│
├── .gitignore
└── README.md
```

---

## ⚙️ Requirements

Before running BITStruq locally, make sure you have:

* Python 3.10 or higher
* pip
* A PostgreSQL/Supabase database
* Gemini API credentials
* Judge0/RapidAPI credentials
* A modern web browser

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/amannraj0/BITStruq.git
cd BITStruq
```

### 2. Set Up the Backend

Navigate to the backend directory:

```bash
cd backend
```

Create a Python virtual environment:

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Inside the `backend` directory, create a `.env` file.

Add the following variables:

```env
GEMINI_API_KEY=your_gemini_api_key
DATABASE_URL=your_database_url
JUDGE0_API_KEY=your_judge0_api_key
```

Replace the placeholder values with your own credentials.

> **Important:** Never commit the `.env` file or expose API keys, database passwords, or other sensitive credentials in the repository.

### 6. Start the Backend

From the `backend` directory, run:

```bash
uvicorn main:app --reload
```

The backend will be available at:

```text
http://127.0.0.1:8000
```

FastAPI interactive documentation is available at:

```text
http://127.0.0.1:8000/docs
```

### 7. Run the Frontend

Open the following file in a modern web browser:

```text
frontend/index.html
```

For full functionality, make sure the FastAPI backend is running.

---

## 🔌 API Endpoints

| Method | Endpoint           | Description                       |
| ------ | ------------------ | --------------------------------- |
| POST   | `/api/ai`          | Generate AI programming responses |
| GET    | `/api/snippets`    | Retrieve saved algorithm snippets |
| POST   | `/api/snippets`    | Save a new algorithm snippet      |
| GET    | `/api/experiences` | Retrieve campus experiences       |
| POST   | `/api/experiences` | Submit a campus experience        |
| POST   | `/api/execute`     | Execute source code using Judge0  |

---

## 🗄️ Database

BITStruq uses PostgreSQL for persistent application data, with Supabase used as the cloud database provider.

The backend stores data related to:

* Algorithm and code snippets
* Campus placement experiences
* Internship experiences

---

## 🔐 Security

* API keys are loaded through environment variables.
* Database credentials are stored outside the source code.
* `.env` is excluded from version control using `.gitignore`.
* `.env.example` is provided as a template for required environment variables.

> Never commit API keys, passwords, database credentials, or other sensitive information to the repository.

---

## 🔮 Future Improvements

* User authentication and authorization
* User-specific developer profiles
* Personalized SQL workspaces
* Enhanced code editor with syntax highlighting
* Support for additional programming languages
* Automated testing and CI/CD
* Dockerized development and deployment
* Improved API documentation

---

## 🤝 Contributing

Contributions, suggestions, and feedback are welcome.

If you would like to contribute:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Commit your changes.
5. Open a pull request.

---

## 👨‍💻 Author

**Aman Raj**

B.Tech — Computer Science & Engineering
Birla Institute of Technology, Mesra

- GitHub: [github.com/amannraj0](https://github.com/amannraj0)
- LinkedIn: [linkedin.com/in/aman-raj-a46aa431b](https://www.linkedin.com/in/aman-raj-a46aa431b)
---


