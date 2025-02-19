import streamlit as st
import segno
from io import BytesIO

def generate_qr_code(url, error_correction='L'):
    qr = segno.make_qr(url, error_correction)
    buffer = BytesIO()
    qr.save(buffer, kind='png', scale=10, border=5)
    buffer.seek(0)
    return buffer

st.title("QR Code Generator")
st.write("""
- **L**: 7% error correction
- **M**: 15% error correction
- **Q**: 25% error correction
- **H**: 30% error correction

Higher levels increase QR code resilience to damage.
""")

url = st.text_input("Enter URL", "https://example.com")
error_correction = st.selectbox("Select Error Correction Level", ['L', 'M', 'Q', 'H'])

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("Generate"):
        qr_buffer = generate_qr_code(url, error_correction)
        st.image(qr_buffer, caption="Generated QR Code", use_container_width=True)
        st.session_state.qr_buffer = qr_buffer
        st.session_state.file_name = f"generated_qr_code_{error_correction}.png"

with col2:
    if 'qr_buffer' in st.session_state:
        st.download_button(
            label="Download QR Code",
            data=st.session_state.qr_buffer,
            file_name=st.session_state.file_name,
            mime="image/png"
        )
    else:
        st.write("First generate, then download.") 