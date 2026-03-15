import streamlit as st
from gtts import gTTS # Thư viện tạo giọng nói miễn phí
import os

st.set_page_config(page_title="App AI cua Thay", layout="wide")

st.title("🎬 AI Video & Voice Studio")

# Ngăn chức năng lồng tiếng
st.header("🔊 Lồng tiếng AI (Miễn phí)")
text_to_speak = st.text_area("Thầy dán đoạn văn cần lồng tiếng vào đây:", 
                             value="Chào mừng quý Thầy Cô đến với VietEdu Smart-Pro 2026.")

if st.button("Chuyển thành giọng nói"):
    if text_to_speak:
        with st.spinner("Đang chuyển ngữ..."):
            # Tạo giọng nói tiếng Việt
            tts = gTTS(text=text_to_speak, lang='vi')
            tts.save("voice.mp3")
            
            # Phát file nhạc ngay trên App
            audio_file = open('voice.mp3', 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3')
            st.success("Đã xong! Thầy có thể nhấn vào 3 dấu chấm ở thanh nhạc để tải về máy.")
    else:
        st.warning("Thầy chưa nhập chữ ạ.")