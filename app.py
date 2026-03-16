import streamlit as st
import cv2
import time

from camera import start_camera, get_frame
from pose_detector import detect_pose
from safety_detection import detect_fall, detect_bad_posture, detect_imbalance
from alert import show_alert, show_warning, show_success


st.set_page_config(page_title="Digital Safety Mirror", layout="wide")

st.title("Digital Safety Mirror")
st.write("AI-based Fall and Posture Detection System")

fps_box = st.sidebar.empty()
status_box = st.sidebar.empty()

cap = start_camera()

frame_window = st.empty()

prev_time = 0

while cap.isOpened():

    frame = get_frame(cap)

    if frame is None:
        st.error("Camera not detected")
        break

    frame, landmarks = detect_pose(frame)

    if landmarks:

        if detect_fall(landmarks):
            show_alert("⚠ Fall Detected")
            status_box.error("Fall Detected")

        elif detect_bad_posture(landmarks):
            show_warning("⚠ Bad Posture")
            status_box.warning("Bad Posture")

        elif detect_imbalance(landmarks):
            show_warning("⚠ Body Imbalance")
            status_box.warning("Imbalance Detected")

        else:
            show_success("Normal Posture")
            status_box.success("System Normal")

    current_time = time.time()
    fps = 1 / (current_time - prev_time) if prev_time != 0 else 0
    prev_time = current_time

    fps_box.metric("FPS", int(fps))

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_window.image(frame)
