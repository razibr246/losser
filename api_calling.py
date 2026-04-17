from google import genai
from dotenv import load_dotenv
from gtts import gTTS
import os
import io

# Loading environment variable
load_dotenv()

my_api_key=os.getenv("GEMNI_API_KEY")

#Initializing a client
client=genai.Client(api_key=my_api_key)

#! Note genarator Function

def note_generator(images):
    prompt = """
Analyze the provided image and generate concise study notes (maximum 100 words) language in English.
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
    response=client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images,prompt] 
    )
    return response.text

#! Audio genarator Function
def audio_transcription(text):
    speech=gTTS(text,lang='en',slow=False)
    audio_buffer=io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return(audio_buffer)

#! Quiz genarator Function
def quiz_generator(image,difficulty):
    prompt = f"Generate 3 quizzes based on {difficulty}.Make sure to add markdown to diffiriancite the options"
    response=client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[image,prompt] 
    )
    return response.text