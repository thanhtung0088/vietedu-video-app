import streamlit as st
import requests

st.set_page_config(page_title="VietEdu AI", layout="wide")
st.title("🎙️ VietEdu AI Studio")

if "FPT_API_KEY" not in st.secrets:
    st.error("Lỗi: Chưa có API Key trong Secrets!")
    st.stop()

text = st.text_area("Nhập nội dung:", "Chào Thầy/cô.")
if st.button("Phát âm"):
    headers = {"api-key": st.secrets["FPT_API_KEY"], "speed": "1", "voice": "banmai"}
    req = requests.post("https://api.fpt.ai/hmi/tts/v5", data=text.encode('utf-8'), headers=headers)
    if req.status_code == 200:
        st.audio(req.json().get("async"))
