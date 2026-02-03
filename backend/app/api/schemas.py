# Request & Response Schemas → Data structures used in API endpoints
from pydantic import BaseModel

class DiseaseResponse(BaseModel):
    crop_name: str
    disease_name: str
    confidence: float
    description: str
    recommended_pesticide: str
    urdu_message: str
    audio_file: str
