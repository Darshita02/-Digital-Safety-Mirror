import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf

mp_pose = mp.solutions.pose

# -------- MediaPipe FULL --------
pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=2,   # FULL model (important)
    enable_segmentation=True,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

def detect_pose_mediapipe(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb)

    keypoints = []
    if results.pose_landmarks:
        for lm in results.pose_landmarks.landmark:
            keypoints.append([lm.x, lm.y, lm.visibility])

    return np.array(keypoints), results


# -------- MoveNet Thunder --------
interpreter = tf.lite.Interpreter(model_path="movenet_thunder.tflite")
interpreter.allocate_tensors()

def detect_pose_movenet(frame):
    img = cv2.resize(frame, (256, 256))
    img = np.expand_dims(img, axis=0).astype(np.int32)

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    interpreter.set_tensor(input_details[0]['index'], img)
    interpreter.invoke()

    keypoints = interpreter.get_tensor(output_details[0]['index'])
    return keypoints