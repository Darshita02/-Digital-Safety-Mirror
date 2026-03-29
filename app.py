import streamlit as st
import cv2
import time

from pose_detector import detect_pose_mediapipe
from preprocessing import preprocess_frame
from smoothing import KeypointSmoother
from alert import trigger_alert

st.title("Digital Safety Mirror")

run = st.checkbox("Start Camera")

cap = cv2.VideoCapture(0)
smoother = KeypointSmoother()

prev_time = 0

while run:
    ret, frame = cap.read()
    if not ret:
        break

    frame = preprocess_frame(frame)

    keypoints, results = detect_pose_mediapipe(frame)

    if len(keypoints) > 0:
        keypoints = smoother.smooth(keypoints)

        # ---- SIMPLE SAFETY LOGIC ----
        # Example: imbalance detection
        left_shoulder = keypoints[11]
        right_shoulder = keypoints[12]

        diff = abs(left_shoulder[1] - right_shoulder[1])

        is_unsafe = diff > 0.1

        if is_unsafe:
            st.error("UNSAFE")
        else:
            st.success("SAFE")

        trigger_alert(is_unsafe)

    # FPS
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    st.write(f"FPS: {int(fps)}")
    st.image(frame, channels="BGR")

cap.release()