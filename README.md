# 🛡️ AI Privacy Shield Pro
**An Enterprise-Grade PII De-identification Engine powered by Llama-3.1-405B.**

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![NVIDIA AI](https://img.shields.io/badge/NVIDIA-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://www.nvidia.com/en-us/ai-on-rtx/)

## 🚀 Overview
**AI Privacy Shield Pro** is a high-performance, containerized web application designed to sanitize sensitive data from text and PDF documents. Unlike traditional regex-based scrubbers, this tool leverages **Large Language Model (LLM) reasoning** to identify PII (Personally Identifiable Information) based on context, ensuring higher accuracy and lower false positives.

### 🏗️ Architecture Flow
![AI Privacy Flow](https://raw.githubusercontent.com/Bhavan790/ai-privacy-shield-pro/main/architecture-diagram.png) 
*(Note: You can replace this link with a screenshot of your dashboard later!)*

### ✨ Key Features
* **Contextual Scrubbing:** Uses **Meta Llama-3.1-405B** (via NVIDIA API) to distinguish between names, locations, and general nouns.
* **Dual-Pane Dashboard:** Modern Glassmorphism UI for side-by-side comparison of Raw vs. Shielded data.
* **PDF Intelligence:** Extracts text from PDFs, scrubs sensitive data, and allows users to download a sanitized PDF report.
* **Dockerized Deployment:** Fully portable environment for consistent performance across any OS.

---

## 🛠️ Tech Stack
* **Backend:** Python / FastAPI
* **AI Engine:** Llama-3.1-405B (NVIDIA NIM API)
* **Document Processing:** PyMuPDF (fitz)
* **Frontend:** Glassmorphism CSS / Vanilla JavaScript
* **DevOps:** Docker

---

## ⚙️ Quick Start

### 1. Clone the Repository
git clone [https://github.com/Bhavan790/ai-privacy-shield-pro.git](https://github.com/Bhavan790/ai-privacy-shield-pro.git)
cd ai-privacy-shield-pro

### 2. Create a .env file in the root directory:
NVIDIA_API_KEY=your_nvidia_api_key_here

### 3. Run the docker
docker build -t privacy-shield .
docker run -p 8000:8000 --env-file .env privacy-shield
Access the dashboard at: http://localhost:8000

Input (Sensitive)                     Output (Shielded)
John Doe lives at 123 Main St.        [PERSON] lives at [ADDRESS].
Call me at 555-0199.                  Call me at [PHONE].

🔒 Security First
* **This project was built with security best practices:

* Zero Data Retention: No data is stored locally; all processing is ephemeral.

* Secret Management: API keys are handled via environment variables and excluded from version control via .gitignore.

* Portability: Containerized via Docker to prevent environment conflicts.

  Developed by BHAVAN
