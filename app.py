import streamlit as st
import requests

st.set_page_config(page_title="VietEdu AI Voice", layout="wide")
st.title("🎙️ VietEdu AI Studio")

if "FPT_API_KEY" not in st.secrets:
    st.error("Chưa cấu hình API Key trong Secrets!")
    st.stop()

text = st.text_area("Nhập văn bản:", "Chào mừng Thầy/cô đến với VietEdu Smart-Pro 2026.")
voice = st.selectbox("Chọn giọng đọc:", ["banmai", "lannhi", "leminh", "myan"])

if st.button("Chuyển thành giọng nói"):
    with st.spinner("Đang xử lý..."):
        headers = {"api-key": st.secrets["FPT_API_KEY"], "voice": voice, "speed": "1"}
        req = requests.post("https://api.fpt.ai/hmi/tts/v5", data=text.encode('utf-8'), headers=headers)
        if req.status_code == 200:
            st.audio(req.json().get("async"))
        else:
            st.error("Lỗi kết nối API.")
