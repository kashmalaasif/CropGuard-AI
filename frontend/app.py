import streamlit as st
import requests
from PIL import Image
import os

# --- Configuration ---
BACKEND_URL = "http://127.0.0.1:8000"
ANALYZE_ENDPOINT = f"{BACKEND_URL}/analyze"

# --- Page Setup ---
st.set_page_config(
    page_title="CropGuard AI",
    page_icon="🌾",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS ---
st.markdown("""
    <style>
    .main {
        background-color: #f0f8ff;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 24px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .result-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    .highlight {
        color: #2e7d32;
        font-weight: bold;
    }
    h1 {
        color: #1b5e20;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
    }
    h3 {
        color: #2e7d32;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Header ---
st.markdown("# 🌾 CropGuard AI")
st.markdown("<p style='text-align: center; color: #555;'>Instant Crop Disease Detection & Urdu Voice Guidance</p>", unsafe_allow_html=True)

st.divider()

# --- Main App Logic ---
uploaded_file = st.file_uploader("Upload a crop leaf image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("🔍 Analyze Crop"):
        with st.spinner("Analyzing image... Please wait..."):
            try:
                # Prepare file for upload
                files = {"image": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                
                # Send request to backend
                response = requests.post(ANALYZE_ENDPOINT, files=files)
                
                if response.status_code == 200:
                    data = response.json()
                    
                    # --- Results Display ---
                    st.markdown("### ✅ Analysis Results")
                    
                    with st.container():
                        st.markdown(f"""
                        <div class="result-card">
                            <p><strong>Crop Name:</strong> <span class="highlight">{data.get('crop_name', 'Unknown')}</span></p>
                            <p><strong>Disease Detected:</strong> <span class="highlight">{data.get('disease_name', 'Unknown')}</span></p>
                            <p><strong>Confidence:</strong> {data.get('confidence', 0) * 100:.1f}%</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        st.progress(data.get('confidence', 0))

                        st.markdown(f"**📝 Description:**\n{data.get('description', 'No description available.')}")
                        
                        st.info(f"**💊 Recommended Pesticide:** {data.get('recommended_pesticide', 'N/A')}")
                        
                        st.markdown("---")
                        
                        # --- Urdu Section ---
                        st.markdown("### 🇵🇰 Urdu Guidance")
                        st.success(f"{data.get('urdu_message', '')}")
                        
                        # --- Audio Player ---
                        audio_path = data.get('audio_file')
                        if audio_path:
                            # If audio_path is just a filename, construct full URL
                            # Assuming backend saves to 'app/audio/' and mounts it at '/audio'
                            # We need to handle how the backend returns the path. 
                            # If it returns a full path or relative path, we might need to adjust.
                            # For now, let's assume we need to point to the static mount.
                            
                            # Clean the path to get just the filename if it's a file path
                            filename = os.path.basename(audio_path)
                            audio_url = f"{BACKEND_URL}/audio/{filename}"
                            
                            st.audio(audio_url, format="audio/mp3")
                        else:
                            st.warning("No audio guidance available.")
                            
                else:
                    st.error(f"Error: {response.text}")
                    
            except requests.exceptions.ConnectionError:
                st.error("🚨 Could not connect to the backend. Is it running? (Create a new terminal and run `uvicorn backend.app.main:app --reload`)")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

# --- Sidebar ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/tractor.png")
    st.markdown("### About CropGuard")
    st.info(
        "CropGuard uses advanced AI to help farmers detect crop diseases early. "
        "Just upload a photo and get instant results with Urdu voice support."
    )
    st.markdown("---")
    st.markdown("Made with ❤️ for Farmers")
