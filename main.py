import os, fitz, requests
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, Response
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
API_KEY = os.getenv("NVIDIA_API_KEY")
URL = "https://integrate.api.nvidia.com/v1/chat/completions"

class TextRequest(BaseModel):
    text: str

def ask_ai_to_scrub(content: str):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "meta/llama-3.1-405b-instruct",
        "messages": [{"role": "user", "content": f"REPLACE all PII (names, emails, phones, addresses) in this text with placeholders like <PERSON> or <EMAIL>. Return ONLY the scrubbed text:\n\n{content}"}],
        "temperature": 0.1
    }
    response = requests.post(URL, headers=headers, json=payload)
    return response.json()['choices'][0]['message']['content']

@app.get("/")
async def get_dashboard():
    return FileResponse("index.html")

@app.post("/scrub")
async def scrub_text(request: TextRequest):
    return {"scrubbed_text": ask_ai_to_scrub(request.text)}

@app.post("/scrub-file")
async def scrub_file(file: UploadFile = File(...)):
    content = ""
    if file.filename.endswith(".pdf"):
        doc = fitz.open(stream=await file.read(), filetype="pdf")
        content = "".join([page.get_text() for page in doc])
    else:
        content = (await file.read()).decode("utf-8")
    return {"scrubbed_text": ask_ai_to_scrub(content)}

@app.post("/download-pdf")
async def download_pdf(request: TextRequest):
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((50, 70), "SHIELDED DOCUMENT REPORT", fontsize=16, color=(0, 0, 1))
    page.insert_textbox((50, 100, 550, 750), request.text, fontsize=11)
    pdf_bytes = doc.write()
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=Shielded_Report.pdf"}
    )