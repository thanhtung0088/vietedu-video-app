import streamlit as st
import requests

st.set_page_config(page_title="VietEdu AI Voice", page_icon="🎙️", layout="wide")
st.title("🎬 AI Video & Voice Studio")
st.subheader("🔊 Lồng tiếng AI đa giọng đọc")

if "FPT_API_KEY" not in st.secrets:
    st.error("❌ Lỗi: Thầy/cô chưa lưu FPT_API_KEY trong phần Secrets!")
    st.stop()

fpt_key = st.secrets["FPT_API_KEY"]

st.write("### 🗣️ Chọn giọng đọc (Speech)")
col_v1, col_v2 = st.columns(2)

with col_v1:
    v_north = st.radio("Giọng miền Bắc:", ["Ban Mai", "Thu Minh", "Lê Minh"])
    v_central = st.radio("Giọng miền Trung:", ["Mỹ An", "Gia Huy", "Ngọc Lam"])

with col_v2:
    v_south = st.radio("Giọng miền Nam:", ["Linh San", "Minh Quang", "Lan Nhi"])
    speed = st.slider("Tốc độ đọc (Speed):", 0.7, 1.5, 1.0, 0.1)

VOICE_MAP = {
    "Ban Mai": "banmai", "Thu Minh": "thuminh", "Lê Minh": "leminh",
    "Mỹ An": "myan", "Gia Huy": "giahuy", "Ngọc Lam": "ngoclam",
    "Linh San": "linhsan", "Minh Quang": "minhquang", "Lan Nhi": "lannhi"
}

selected_voice = VOICE_MAP[v_south] if v_south else VOICE_MAP[v_north]

st.write("---")
text_input = st.text_area("Thầy/cô dán văn bản cần lồng tiếng vào đây:", height=200)

if st.button("🚀 Chuyển thành giọng nói"):
    if text_input.strip():
        with st.spinner("Đang xử lý..."):
            headers = {"api-key": fpt_key, "speed": str(speed), "voice": selected_voice}
            req = requests.post("https://api.fpt.ai/hmi/tts/v5", data=text_input.encode('utf-8'), headers=headers)
            if req.status_code == 200:
                audio_url = req.json().get("async")
                st.success("✅ Đã xong!")
                st.audio(audio_url)
            else:
                st.error("Lỗi kết nối FPT AI. Thầy/cô kiểm tra lại API Key nhé.")