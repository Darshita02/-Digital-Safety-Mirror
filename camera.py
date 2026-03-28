import cv2

def start_camera():
    return cv2.VideoCapture(0)

def get_frame(cap):
    ret, frame = cap.read()
    if not ret:
        return None

    frame = cv2.flip(frame, 1)
    return frame

def release_camera(cap):
    cap.release()