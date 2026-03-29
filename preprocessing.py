import cv2

def preprocess_frame(frame):
    # Blur reduction (sharpening)
    kernel = [[0, -1, 0], [-1, 5,-1], [0, -1, 0]]
    frame = cv2.filter2D(frame, -1, kernel)

    return frame


def stabilize_frame(prev_frame, curr_frame):
    # simple stabilization (can be improved)
    return curr_frame