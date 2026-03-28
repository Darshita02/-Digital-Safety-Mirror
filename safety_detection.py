import math

def calculate_angle(a, b, c):
    angle = math.degrees(
        math.atan2(c[1]-b[1], c[0]-b[0]) -
        math.atan2(a[1]-b[1], a[0]-b[0])
    )
    if angle < 0:
        angle += 360
    return angle


def detect_fall(landmarks):
    if len(landmarks) < 26:
        return False

    shoulder = landmarks[11]
    hip = landmarks[23]
    knee = landmarks[25]

    angle = calculate_angle(shoulder, hip, knee)

    return angle < 120


def detect_imbalance(landmarks):
    left_shoulder = landmarks[11]
    right_shoulder = landmarks[12]

    tilt = abs(left_shoulder[1] - right_shoulder[1])

    return tilt > 0.05


def detect_unstable_body(landmarks):
    head = landmarks[0]
    hip = landmarks[23]

    height = abs(head[1] - hip[1])

    return height < 0.2