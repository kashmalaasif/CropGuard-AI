from fastapi import FastAPI, APIRouter, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.services.image_processing import validate_image, preprocess_image
from app.api.routes import router
from app.api.schemas import DiseaseResponse
import os
from fastapi.staticfiles import StaticFiles

load_dotenv()

app = FastAPI(
    title="CropGuard AI Backend",
    description="AI-powered crop disease detection with voice support",
    version="1.0.0"
)

# CORS (safe default)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)  #app.include_router(router, prefix="/api")

# Make mp3 accessible via URL
app.mount("/audio", StaticFiles(directory="app/audio"), name="audio")

@app.get("/")  
def root():
    return {"message": "CropGuard AI Backend is running 🚀"}

# @app.get("/health")
# def health_check():
#     return {"status": "Backend is running 🚀"}

# @app.post("/predict")
# async def predict_disease(file: UploadFile = File(...)):
#     if not file.content_type.startswith("image/"):
#         raise HTTPException(status_code=400, detail="Please upload an image file")

#     image_bytes = await file.read()

#     try:
#         image = validate_image(image_bytes)
#         processed_image = preprocess_image(image)
#     except ValueError as e:
#         raise HTTPException(status_code=400, detail=str(e))

#     return {
#         "filename": file.filename,
#         "message": "Image validated and processed successfully ✅",
#         "processed_size_bytes": len(processed_image)
#     }
