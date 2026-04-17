import streamlit as st
from api_calling import note_generator
from api_calling import audio_transcription
from api_calling import quiz_generator
from PIL import Image
 #!Header Part
st.title("Note summary and Quiz Generator",anchor=False)
st.markdown("Upload upto 3 images to generate Note summary and Quizzes")
st.divider()

 #?Sidebar
 
with st.sidebar:
    st.header("Controls")
    #& Work with images here
    images=st.file_uploader(
        "Upload your image here for getting Notes",
        type=['jpg','jpeg','png'],
        accept_multiple_files=True
    )
    pil_images=[]
    for img in images:
        pil_img=Image.open(img)
        pil_images.append(pil_img)
        
    if images:
        if len(images)>3:
            st.error("You can't upload more than 3 images")
        else:
            st.subheader("Uploaded images")
            col=st.columns(len(images))
            
            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)
    #& Work with category
    selected_option=st.selectbox(
        "Select the Quiz Difficulty",
        ("Easy","Medium","Hard"),
        index=None
    )
    if selected_option:
        st.markdown(f"You selected **{selected_option}** as difficulty of your quiz")
    pressed=st.button("Submit to Generate",type="primary")
    
if pressed:
    if not images:
        st.error("You have to upload at least 1 Image")
    if not selected_option:
        st.error("You have to select a difficulty level")
    
    if images and selected_option:
        #note
        with st.container(border=True):
            st.subheader("Your notes",anchor=False)
            with st.spinner("Please wait, Generating notes"):
                
                generate_notes=note_generator(pil_images)
                st.markdown(generate_notes)
        #Audio Transcript
        with st.container(border=True):
            st.subheader("Audio Transcript",anchor=False)
            with st.spinner("Generating Transcript"):
                # clearing markdown
                generate_notes=generate_notes.replace("#","")
                generate_notes=generate_notes.replace("*","")
                generate_notes=generate_notes.replace("_","")
                audio_transcription=audio_transcription(generate_notes)
                st.audio(audio_transcription)
            
        #Quiz section
        with st.container(border=True):
            st.subheader(f"Quiz **({selected_option})** Difficulty",anchor=False)
    
            with st.spinner("Generating Quizzes please wait !"):
                quizzes = quiz_generator(pil_images, selected_option)
                st.markdown(quizzes)