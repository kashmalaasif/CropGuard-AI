# 🌱 CropGuard – AI-Powered Crop Disease Detection

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python"/>
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi"/>
  <img src="https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit"/>
  <img src="https://img.shields.io/badge/Google-Gemini%20AI-4285F4?logo=google"/>
  <img src="https://img.shields.io/badge/Swagger-API%20Docs-85EA2D?logo=swagger"/>
  <img src="https://img.shields.io/badge/Dotenv-Environment-yellow"/>
</p>

CropGuard is an **AI-powered crop disease detection system** that analyzes crop leaf images using **Google Gemini Vision models** and provides:
- Crop name
- Disease name
- Confidence score
- Description
- Recommended pesticide
- Urdu guidance for farmers 🇵🇰

---

## 🚀 Tech Stack

| Layer | Technology |
|------|------------|
| Backend API | FastAPI |
| AI Model | Google Gemini Vision |
| Frontend | Streamlit |
| Image Processing | Pillow |
| API Docs | Swagger (OpenAPI) |
| Environment | Python 3.11 |

---

## 📂 Project Structure

```text

CropGuard-AI/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── routes.py
│   │   │   └── schemas.py
│   │   ├── services/
│   │   │   ├── gemini_client.py
│   │   │   ├── image_processing.py
│   │   │   └── voice_service.py
│   │   ├── main.py    # FastAPI app + endpoints
|   |   └── .gitignore 
│
├── frontend/
│   
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/cropguard-backend.git
cd cropguard-backend
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Environment Variables
Create a `.env` file:
```env
PORT=8000
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-3-flash-preview
```

### 5️⃣ Run Backend
```bash
uvicorn app.main:app --reload
```

API will be live at:
👉 http://127.0.0.1:8000  
👉 Swagger Docs: http://127.0.0.1:8000/docs

---

## 🖥️ Streamlit Frontend (Optional)

```bash
streamlit run app.py
```

Streamlit can be used to:
- Upload crop images
- Preview predictions visually
- Show Urdu guidance to farmers

---

## 🔌 API Endpoint

### `POST /analyze`

**Input:** Multipart image file  
**Output:** JSON response

```json
{
  "crop_name": "Wheat",
  "disease_name": "Leaf Rust",
  "confidence": 0.95,
  "description": "Fungal disease affecting wheat leaves.",
  "recommended_pesticide": "Propiconazole",
  "urdu_message": "یہ گندم کی بیماری ہے۔"
}
```

---

## 👩‍💻 Team

| Name | Role | GitHub |
|-----|------|--------|
| Hanif Ullah | Team Lead, Frontend Developer| https://github.com/hanifullah313 |
| Moneka Meghwar | Backend Developer, API Integration | https://github.com/mmoneka11 |
| Kashmala Asif | Documentation Lead, Development Support| https://github.com/kashmalaasif |


---

## 🔐 Security Notes

- .env is ignored via .gitignore
- API keys are never exposed

---

## 📌 Future Enhancements
- Mobile App (Flutter)
- Multi-language farmer support
- Offline disease detection
- Crop advisory dashboard

---

## 📜 License
MIT License

---

✨ Built with ❤️ for smart agriculture
