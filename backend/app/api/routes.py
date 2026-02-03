# → API logic - Image Upload Route
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.api.schemas import DiseaseResponse
from app.services.image_processing import validate_image, preprocess_image
from app.services.gemini_client import analyze_crop_disease
from app.services.voice_service import text_to_voice

router = APIRouter()

@router.post("/analyze", response_model=DiseaseResponse)
async def analyze_crop_image(image: UploadFile = File(...)):
    """
    Receives an image and returns disease analysis
    (Gemini logic will be added in next steps)
    Image → Validation → Preprocessing → Gemini → JSON → API Response
    """
    try:
        # Read uploaded image
        image_bytes = await image.read()

        # Validate & preprocess
        image_obj = validate_image(image_bytes)
        processed_image = preprocess_image(image_obj)

        # CALL GEMINI HERE
        ai_result = analyze_crop_disease(processed_image)
        
        # Generate voice message     
        audio_path = text_to_voice(ai_result["urdu_message"], lang="ur")  # Get Urdu text Call Voice API
        ai_result["audio_file"] = audio_path    # Attach audio

        return DiseaseResponse(**ai_result)

        # Temporary dummy response (will replace with AI output)
        # return DiseaseResponse(
        #     crop_name="Wheat",
        #     disease_name="Leaf Rust",
        #     confidence=0.92,
        #     description="A fungal disease affecting wheat leaves.",
        #     recommended_pesticide="Propiconazole",
        #     urdu_message="یہ گندم کی پتیوں کی بیماری ہے۔ تجویز کردہ دوا پروپیکونازول ہے۔" )

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
 
