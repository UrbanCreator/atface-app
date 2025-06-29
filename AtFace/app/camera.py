import cv2
import os
import platform

def capture_video(source=None):
    """
    Initializes video capture.
    - If `source` is None, uses the default webcam (platform-independent).
    - If `source` is a string path to a file, uses that file as input.
    """
    if source is not None and os.path.isfile(source):
        return cv2.VideoCapture(source)

    # Webcam capture (index 0 is cross-platform)
    return cv2.VideoCapture(0)

def draw_faces(frame, recognized_faces):
    for name, (top, right, bottom, left) in recognized_faces:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
