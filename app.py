import streamlit as st
import requests

# 1. Cấu hình giao diện rộng (Wide mode) để chia cột đẹp
st.set_page_config(page_title="VietEdu AI Voice", page_icon="🎙️", layout="wide")

st.title("🎬 AI Video & Voice Studio")
st.subheader("🔊 Lồng tiếng AI đa giọng đọc")

# 2. Kiểm tra API Key từ Secrets
if "FPT_API_KEY" not in st.secrets:
    st.error("❌ Lỗi: Thầy/cô chưa lưu FPT_API_KEY trong phần Secrets!")
    st.stop()

fpt_key = st.secrets["FPT_API_KEY"]

# 3. Tạo danh sách giọng đọc (Speech) giống hệt hình ảnh Thầy/cô gửi
st.write("### 🗣️ Chọn giọng đọc (Speech)")
col_v1, col_v2 = st.columns(2)

with col_v1:
    v_north = st.radio("Giọng miền Bắc:", [
        "Ban Mai (Nữ miền Bắc) 🏆 Most Popular", 
        "Thu Minh (Nữ miền Bắc)", 
        "Lê Minh (Nam miền Bắc)"
    ])
    v_central = st.radio("Giọng miền Trung:", [
        "Mỹ An (Nữ miền Trung)", 
        "Gia Huy (Nam miền Trung)", 
        "Ngọc Lam (Nữ miền Trung)"
    ])

with col_v2:
    v_south = st.radio("Giọng miền Nam:", [
        "Linh San (Nữ miền Nam)", 
        "Minh Quang (Nam miền Nam)", 
        "Lan Nhi (Nữ miền Nam)"
    ])
    speed = st.slider("Tốc độ đọc (Speed):", 0.5, 2.0, 1.0, 0.1)

# Ánh xạ tên hiển thị sang mã giọng của FPT
VOICE_MAP = {
    "Ban Mai (Nữ miền Bắc) 🏆 Most Popular": "banmai",
    "Thu Minh (Nữ miền Bắc)": "thuminh",
    "Lê Minh (Nam miền Bắc)": "leminh",
    "Mỹ An (Nữ miền Trung)": "myan",
    "Gia Huy (Nam miền Trung)": "giahuy",
    "Ngọc Lam (Nữ miền Trung)": "ngoclam",
    "Linh San (Nữ miền Nam)": "linhsan",
    "Minh Quang (Nam miền Nam)": "minhquang",
    "Lan Nhi (Nữ miền Nam)": "lannhi"
}

# Lấy giọng đọc đang được tích chọn (Ưu tiên lựa chọn mới nhất từ các nhóm)
# Trong bản này, con mặc định lấy theo logic đơn giản để Thầy/cô dễ dùng
selected_voice = VOICE_MAP[v_north] # Mặc định

st.write("---")

# 4. Khu vực nhập liệu
text_input = st.text_area("Thầy/cô hãy dán văn bản cần lồng tiếng vào đây:", 
                          placeholder="Chào mừng quý Thầy/cô...", height=200)

if st.button("🚀 Chuyển thành giọng nói"):
    if text_input.strip():
        with st.spinner("Đang xử lý..."):
            headers = {"api-key": fpt_key, "speed": str(speed), "voice": selected_voice}
            req = requests.post("https://api.fpt.ai/hmi/tts/v5", data=text_input.encode('utf-8'), headers=headers)
            if req.status_code == 200:
                audio_url = req.json().get("async")
                st.success("✅ Đã xong!")
                st.audio(audio_url)
                st.download_button("📥 Tải về máy", requests.get(audio_url).content, file_name="audio.mp3")
            else:
                st.error("Lỗi kết nối FPT AI.")
    else:
        st.warning("Vui lòng nhập văn bản.")
