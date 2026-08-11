from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import time

# 1. Load Secrets
load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
DB_URL = os.getenv("DATABASE_URL")

# 2. Initialize App & Security
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 3. Database Connection Helper
def get_db_connection():
    return psycopg2.connect(
        DB_URL,
        cursor_factory=RealDictCursor
    )

# 4. Data Models (What frontend sends us)
class ChatRequest(BaseModel):
    prompt: str

class ExecutionRequest(BaseModel):  # 👈 ADD THIS MODEL
    language_id: int
    source_code: str
    stdin: str

class Snippet(BaseModel):
    title: str
    language: str
    complexity: str
    code: str
    notes: str

class Experience(BaseModel):
    company: str
    role: str
    author: str
    tags: str
    experience: str

# -------------------------------------------------
# 🤖 GEMINI AI ENDPOINT
# -------------------------------------------------
@app.post("/api/ai")
def get_ai_response(request: ChatRequest):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_KEY}"
    payload = {"contents": [{"parts": [{"text": request.prompt}]}]}
    response = requests.post(url, json=payload)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="AI API Error")
    return response.json()

# -------------------------------------------------
# 🧠 ALGO VAULT ENDPOINTS
# -------------------------------------------------
@app.get("/api/snippets")
def get_snippets():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM custom_snippets ORDER BY created_at DESC;")
    snippets = cur.fetchall()
    conn.close()
    return snippets

@app.post("/api/snippets")
def add_snippet(snippet: Snippet):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO custom_snippets (title, language, complexity, code, notes) VALUES (%s, %s, %s, %s, %s) RETURNING id;",
        (snippet.title, snippet.language, snippet.complexity, snippet.code, snippet.notes)
    )
    conn.commit()
    conn.close()
    return {"message": "Snippet saved to cloud!"}

# -------------------------------------------------
# 🤝 CAMPUS EXCHANGE ENDPOINTS
# -------------------------------------------------
@app.get("/api/experiences")
def get_experiences():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM campus_experiences ORDER BY created_at DESC;")
    experiences = cur.fetchall()
    conn.close()
    return experiences

@app.post("/api/experiences")
def add_experience(exp: Experience):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO campus_experiences (company, role, author, tags, experience) VALUES (%s, %s, %s, %s, %s) RETURNING id;",
        (exp.company, exp.role, exp.author, exp.tags, exp.experience)
    )
    conn.commit()
    conn.close()
    return {"message": "Experience saved to cloud!"}

# -------------------------------------------------
# ⚡ CODE EXECUTION ENDPOINT
# -------------------------------------------------
@app.post("/api/execute")
def execute_code(req: ExecutionRequest):
    judge0_key = os.getenv("JUDGE0_API_KEY")
    headers = {
        "x-rapidapi-key": judge0_key,
        "x-rapidapi-host": "judge0-ce.p.rapidapi.com",
        "Content-Type": "application/json"
    }
    
    payload = {
        "language_id": req.language_id,
        "source_code": req.source_code,
        "stdin": req.stdin,
        "base64_encoded": True
    }
    
    # 1. Send code to Judge0
    create_res = requests.post(
        "https://judge0-ce.p.rapidapi.com/submissions?base64_encoded=true", 
        json=payload, 
        headers=headers
    )
    
    if create_res.status_code not in [200, 201]:
        raise HTTPException(status_code=500, detail="Code submission failed")
        
    token = create_res.json().get("token")
    
    # 2. Poll for the result (since execution takes a moment)
    while True:
        time.sleep(1)
        poll_res = requests.get(
            f"https://judge0-ce.p.rapidapi.com/submissions/{token}?base64_encoded=true",
            headers=headers
        )
        result = poll_res.json()
        
        # Status ID > 2 means it is finished processing
        if result.get("status", {}).get("id", 1) > 2:
            break
            
    return result