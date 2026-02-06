# 🌾 CropGuard: AI-Powered Crop Disease Dignosis
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python"/>
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi"/>
  <img src="https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit"/>
  <img src="https://img.shields.io/badge/Google-Gemini%20AI-4285F4?logo=google"/>
  <img src="https://img.shields.io/badge/Swagger-API%20Docs-85EA2D?logo=swagger"/>
  <img src="https://img.shields.io/badge/Dotenv-Environment-yellow"/>
</p>

**Event:** DevLaunch Hackathon 2026 (WPBrigade × iCodeGuru)

CropGuard is a multi-modal AI-powered system designed to assist traditional farmers by detecting crop diseases from leaf images and providing **spoken Urdu guidance**. The platform leverages state-of-the-art **computer vision, natural language processing, and speech synthesis** to make advanced agricultural intelligence accessible to non-technical users.

The system allows farmers to simply upload a crop image. The AI then identifies the crop and disease, explains the issue in English, translates the result into Urdu, and finally converts it into **natural Urdu voice output**, enabling farmers to interact with the system without needing literacy or technical skills. 

---

## 🎯 Project Overview

CropGuard addresses a real-world problem in agriculture:  
**farmers lack instant access to expert-level crop disease diagnosis.**

By using modern AI models, CropGuard provides:

- Crop name detection  
- Disease identification  
- Confidence score  
- Disease description  
- Recommended pesticide  
- **Urdu text guidance**  
- **Urdu voice assistance (hands-free)**  

This project demonstrates an end-to-end **multi-modal AI system** combining:

- Vision AI  
- NLP translation  
- Speech synthesis  

Built as a **hackathon demo**, but architected to be **scalable and production-ready**.

---

## 🎥 Demo Video (YouTube)

Watch the complete demo of **CropGuard – AI-Powered Crop Disease Dignosis**:
<p align="center">
  <a href="https://youtu.be/GdT-lj6J7Bk" target="_blank">
    <img src="https://img.youtube.com/vi/GdT-lj6J7Bk/0.jpg" 
         alt="CropGuard AI Demo Video" 
         width="70%">
    <br>▶️ Click to Play
  </a>
</p>

---


## 🏗️ System Architecture

### Three-Tier Architecture

| Layer | Description |
|------|-------------|
| Presentation Layer | Streamlit web interface for farmers |
| Application Layer | FastAPI backend for request handling |
| AI Layer | Gemini Flash 3 (Vision) + Gemini NLP + Google Voice API |

### AI Processing Flow

```mermaid
graph TD
    A[Crop Image Upload] --> B[Gemini Flash 3 Vision Mode]
    B --> C[ Disease Diagnosis]
    C --> D[Gemini Translation API]
    D --> E[Urdu Text]
    E --> F[Google Voice API]
    F --> G[Urdu Voice Output for Farmer]
```

This makes CropGuard a **fully multi-modal AI pipeline**:  
**Image → Text → Translation → Speech**

---

## 🚀 Technology Stack

### Backend

| Component | Technology |
|----------|------------|
| API Framework | FastAPI |
| AI Vision Model | Google Gemini Flash 3 |
| Image Processing | Pillow |
| Translation | Gemini Text API |
| Voice | Google Voice API |
| Environment | Python 3.11 |
| API Docs | Swagger (OpenAPI) |

### Frontend

| Component | Technology |
|----------|------------|
| UI | Streamlit |
| User Interaction | Image upload + audio output |
| Target Users | Traditional farmers |

---

## 🧠 AI Model & Intelligence Pipeline

### Gemini Flash 3 (Vision AI)

Gemini Flash 3 is a lightweight and high-performance multimodal model capable of understanding images and generating structured textual outputs.

In CropGuard, Gemini Flash 3 is used to:

- Analyze crop leaf images  
- Identify crop type  
- Detect disease patterns  
- Generate human-readable diagnosis  

### Language & Voice Intelligence

After vision inference:

1. Output is generated in **English**  
2. Gemini Translation API converts English → **Urdu**  
3. Google Voice API converts Urdu text → **natural Urdu speech**

This enables:

- Voice-based interaction  
- Accessibility for illiterate farmers  
- Real-world usability in rural Pakistan  

---

## 📊 Supported Crops

CropGuard is designed to work with **multiple crop types**, including but not limited to:

- Wheat  
- Rice  
- Cotton  
- Tomato  
- Potato  
- Sugarcane  
- Maize  
- Vegetables and fruits  

The system is **model-agnostic** and can scale to more crops without retraining.

---

## 🔬 Testing & Evaluation

Since this project is based on **real-time AI inference (no custom training)**, evaluation was performed through:

- Manual testing on multiple crop images  
- Cross-verification with online agricultural sources  
- Live testing during hackathon demo  

The system demonstrated:

- High confidence predictions for common crops  
- Accurate disease identification for visible symptoms  
- Consistent translation and voice generation  

This validates CropGuard as a **practical real-world AI assistant**, not just a theoretical model.

---

## 🚀 Deployment Architecture

### Current Status

- **Hackathon Demo Deployment**  
- Runs locally with full functionality  
- Scalable microservice design  

### Scalable by Design

The system can be deployed to:

- Cloud platforms (Render, AWS, GCP, Azure)  
- Mobile apps (Flutter / React Native)  
- IoT devices (field cameras)  

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
│   └── app.py
├── .env
├── requirements.txt
└── README.md
```

---
## 🔌 API Endpoint

### POST `/analyze`

**Input:** Multipart image file  
**Output:** JSON response

```json
{
  "crop_name": "Wheat",
  "disease_name": "Leaf Rust",
  "confidence": 0.95,
  "description": "Fungal disease affecting wheat leaves.",
  "recommended_pesticide": "Propiconazole",
  "urdu_message": "یہ گندم کی بیماری ہے اور اس کے علاج کے لیے مخصوص دوا استعمال کریں۔"
}

```
---

## ⚙️ Local Installation & Usage

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
Create a .env file in the root directory:

**PORT**=8000
**GEMINI_API_KEY**=GOOGLE VOICE API + GEMINI API 
**GEMINI_MODEL**=gemini-3-flash-preview
### 5️⃣ Run Backend
uvicorn app.main:app --reload
🔌 API Access
**Base URL:** http://127.0.0.1:8000

**Swagger Docs: **http://127.0.0.1:8000/docs

---
## 🖥️ Streamlit Frontend
Run the Streamlit application:

streamlit run app.py
The frontend allows farmers to:

Upload crop images

View disease predictions

Receive Urdu guidance

Listen to voice instructions

---
## 🔐 Security Notes
.env file is ignored via .gitignore

API keys are never committed to the repository

No sensitive data is stored

All inference is stateless and secure

---
## 🎯 Key Achievements
Multi-modal AI system (Vision + NLP + Voice)

Real-world agricultural use case

Built for non-technical users

Urdu voice accessibility 🇵🇰

Scalable microservice architecture

Production-ready design

Hackathon-grade innovation

---
## 🔮 Future Enhancements
- Mobile app (Flutter)

- Offline disease detection

- Multi-language farmer support

- Crop advisory dashboard

- IoT camera integration

- Government agriculture data APIs

- Model fine-tuning on local Pakistani crops

---
## 👥 Team
| Name              | Role                                    | GitHub                                                               |
| ----------------- | --------------------------------------- | -------------------------------------------------------------------- |
| Hanif Ullah       | Team Lead, Frontend Developer           | [https://github.com/hanifullah313](https://github.com/hanifullah313) |
| Moneka Meghwar    | Backend Developer, API Integration      | [https://github.com/mmoneka11](https://github.com/mmoneka11)         |
| Kashmala Saddiqui | Documentation Lead,API Integrate Support| [https://github.com/kashmalaasif](https://github.com/kashmalaasif)   |
| Osama             | Streamlit Integrator / Developer        | [https://github.com/Osama2321](https://github.com/Osama2321)         |
---
## 📜 License

This project is licensed under the MIT License.

---
## 🤝 Contributing

We welcome contributions! Please open issues or pull requests.

⭐ **Support this project:** If you find this project useful, please star the repo!
[![GitHub stars](https://img.shields.io/github/stars/mmoneka11/CropGuard-AI?style=social)](https://github.com/mmoneka11/CropGuard-AI/stargazers)

✨ Built with ❤️ for smart agriculture
