import streamlit as st
import cv2

from camera import start_camera, get_frame, release_camera
from pose_detector import detect_pose
from safety_detection import detect_fall, detect_imbalance, detect_unstable_body
from alert import show_alert, show_success, play_sound, send_sms_alert

st.title("🪞 Digital Safety Mirror")

run = st.checkbox("Start Camera")

FRAME_WINDOW = st.image([])

cap = start_camera()

unsafe_frames = 0
THRESHOLD = 8
alert_sent = False

while run:
    frame = get_frame(cap)

    if frame is None:
        break

    landmarks = detect_pose(frame)

    if landmarks:
        fall = detect_fall(landmarks)
        imbalance = detect_imbalance(landmarks)
        unstable = detect_unstable_body(landmarks)

        if fall or imbalance or unstable:
            unsafe_frames += 1
        else:
            unsafe_frames = 0

        if unsafe_frames > THRESHOLD:
            show_alert("⚠ Unsafe Condition Detected!")
            play_sound()

            if not alert_sent:
                send_sms_alert()
                alert_sent = True
        else:
            show_success("Safe")
            alert_sent = False

    FRAME_WINDOW.image(frame, channels="BGR")

release_camera(cap)
