import os
import json
import re
import time
from google import genai
from google.genai import types
from google.genai.errors import ClientError
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("❌ Error: GEMINI_API_KEY is missing from .env file!")

client = genai.Client(api_key=api_key)

def analyze_crop_disease(image_bytes: bytes) -> dict:
    image_part = types.Part.from_bytes(
        data=image_bytes,
        mime_type="image/jpeg"
    )

    prompt = """
        You are an agricultural expert for Pakistan.
        Analyze the crop leaf image and respond ONLY in valid JSON:
        {
        "crop_name": "",
        "disease_name": "",
        "confidence": 0.0,
        "description": "",
        "recommended_pesticide": "",
        "urdu_message": ""
        }
        """

    # We use 'gemini-flash-latest' because it was in your list
    # and it usually has the highest free limits (15 RPM).
    try:
        response = client.models.generate_content(
            model="gemini-flash-latest", 
            contents=[prompt, image_part]
        )
        
        text = response.text or ""
        text = text.replace("```json", "").replace("```", "").strip()
        
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if not match:
            raise ValueError("Gemini response was not valid JSON.")
            
        return json.loads(match.group())

    except ClientError as e:
        print(f"❌ API Error: {e}")
        raise e