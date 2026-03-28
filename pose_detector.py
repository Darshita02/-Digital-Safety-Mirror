import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose

pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=2,
    enable_segmentation=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

prev_landmarks = None

def smooth_landmarks(current, prev, alpha=0.7):
    if prev is None:
        return current

    smoothed = []
    for c, p in zip(current, prev):
        x = alpha * p[0] + (1 - alpha) * c[0]
        y = alpha * p[1] + (1 - alpha) * c[1]
        smoothed.append((x, y))

    return smoothed


def detect_pose(frame):
    global prev_landmarks

    # Preprocessing
    frame = cv2.GaussianBlur(frame, (5, 5), 0)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = pose.process(rgb)

    if result.pose_landmarks:
        landmarks = [(lm.x, lm.y) for lm in result.pose_landmarks.landmark]

        landmarks = smooth_landmarks(landmarks, prev_landmarks)
        prev_landmarks = landmarks

        return landmarks

    return None
    