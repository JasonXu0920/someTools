import streamlit as st
import time
import numpy as np
from pydub import AudioSegment, silence
import speech_recognition as sr
import os

st.set_page_config(page_title="Audio To Text", page_icon="📈")

recognize = sr.Recognizer()
final_result = ""
st.markdown("<h1 style='text-align:center;'>Audio To Text Converter</h1>", unsafe_allow_html=True)
st.markdown("---", unsafe_allow_html=True)

audio = st.file_uploader("Upload Your Audio File", type=['mp3', 'wav', 'aac'])
if audio:
    st.audio(audio)
    audio_segment = AudioSegment.from_file(audio)
    chunks = silence.split_on_silence(audio_segment,min_silence_len=500,silence_thresh=audio_segment.dBFS-20,keep_silence=100)  
    for i, chunk in enumerate(chunks):
        chunk.export(str(i)+".wav", format="wav")
        with sr.AudioFile(str(i)+"wav") as source:
            recorded = recognize.record(source)
            try:
                text = recognize.recognize_google(recorded)
                final_result+=" "
                final_result+=text
            except:
                print("Invalid chunk of audio")
                final_result+=" "
                final_result+= "None"
    with st.form("Transcript"):
        result = st.text_area("TEXT", value=final_result)
        d_btn = st.form_submit_button("Download")
        if d_btn:
            envir_var = os.environ.get("USERPROFILE")+"\Downloads\\transcript.txt"
            with open(envir_var, 'w') as file:
                file.write(result)
