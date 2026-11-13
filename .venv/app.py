import streamlit as st
from ultralytics import YOLO
from PIL import Image
import torch


st.set_page_config(
    page_title="VisionPort",
    page_icon="🚗",
    layout="wide",
)

st.title("VisionPort v0.1")
st.write(
    "GPU-Accelerated Traffic Object Detection"
)

device ="cuda" if torch.cuda.is_available() else "cpu"
st.write(f"Running on:**{device.upper()}**")

@st.cache_resource
def load_model():

    model = YOLO("yolov8n.pt")

    return model

model = load_model()

uploaded_file = st.file_uploader(
    "Upload a traffic image",
    type=["jpg", "jpeg", "png"],
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.subheader("Original Image")

    st.image(
        image,
        caption="Upload traffic image",
        use_container_width=True
    )

    results = model.predict(
        source=image,
        device=device
    )

    result_image = results[0].plot()

    st.subheader("Detection Result")
    st.image(
        result_image,
        caption="Detected Objects",
        channels="BGR",
        use_container_width=True
    )