import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

pose = mp_pose.Pose()

def detect_pose(frame):

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)

    landmarks = []

    if results.pose_landmarks:
        for lm in results.pose_landmarks.landmark:
            h, w, _ = frame.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            landmarks.append((cx, cy))

        mp_drawing.draw_landmarks(
            frame,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS
        )

    return frame, landmarks
    