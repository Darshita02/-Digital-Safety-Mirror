import numpy as np

class KeypointSmoother:
    def __init__(self, window=5):
        self.window = window
        self.buffer = []

    def smooth(self, keypoints):
        self.buffer.append(keypoints)

        if len(self.buffer) > self.window:
            self.buffer.pop(0)

        return np.mean(self.buffer, axis=0)