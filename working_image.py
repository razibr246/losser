import streamlit as st
from google import genai
from dotenv import load_dotenv
import os
from PIL import Image
# Load environment variables
load_dotenv()

my_api_key = os.getenv("GEMNI_API_KEY")

# Initialize client
client = genai.Client(api_key=my_api_key)

# File uploader
images = st.file_uploader(
    "Upload your image here for getting Notes",
    type=['jpg', 'jpeg', 'png'],
    accept_multiple_files=True
)

# Prompt
prompt = """
Analyze the provided image and generate concise study notes (maximum 100 words).

Requirements:
- Use clear markdown formatting.
- Include a short title.
- Use bullet points for key information.
- Highlight important terms in bold.
- If the image contains text, extract and summarize it.
- If it is a diagram, explain it simply.

Output format example:
# Title

- Point 1
- Point 2
- Point 3
"""

# Processing images
if images:
    pil_images=[]
    for img in images:
        pil_img=Image.open(img)
        pil_images.append(pil_img)
    for img in images:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=[pil_images, prompt]
        )

        st.markdown(response.text)
        st.divider()