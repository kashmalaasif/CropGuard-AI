# Gemini Client Service

import os
import json
import re
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

# Create/Configure Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

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

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[prompt, image_part]
    )

    # print("====== RAW GEMINI OUTPUT ======")  #Debug
    # print(response.text)

    text = response.text or ""

    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("Gemini response not in JSON format")

    return json.loads(match.group())
