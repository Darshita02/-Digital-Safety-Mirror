import math

def calculate_angle(a, b, c):
    ax, ay = a
    bx, by = b
    cx, cy = c

    angle = math.degrees(
        math.atan2(cy - by, cx - bx) -
        math.atan2(ay - by, ax - bx)
    )

    if angle < 0:
        angle += 360

    return angle


def detect_fall(landmarks):
    shoulder = landmarks[11]
    hip = landmarks[23]

    if abs(shoulder[1] - hip[1]) < 30:
        return True
    return False


def detect_bad_posture(landmarks):
    shoulder = landmarks[11]
    ear = landmarks[7]

    if abs(shoulder[0] - ear[0]) > 40:
        return True
    return False


def detect_imbalance(landmarks):
    left_hip = landmarks[23]
    right_hip = landmarks[24]

    if abs(left_hip[1] - right_hip[1]) > 35:
        return True
    return False