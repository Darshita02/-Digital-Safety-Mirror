def detect_fall(landmarks):

    if len(landmarks) < 25:
        return False

    shoulder = landmarks[11]
    hip = landmarks[23]

    if abs(shoulder[1] - hip[1]) < 30:
        return True

    return False


def detect_bad_posture(landmarks):

    if len(landmarks) < 12:
        return False

    shoulder = landmarks[11]
    ear = landmarks[7]

    if abs(shoulder[0] - ear[0]) > 40:
        return True

    return False


def detect_imbalance(landmarks):

    if len(landmarks) < 25:
        return False

    left_hip = landmarks[23]
    right_hip = landmarks[24]

    if abs(left_hip[1] - right_hip[1]) > 35:
        return True

    return False
