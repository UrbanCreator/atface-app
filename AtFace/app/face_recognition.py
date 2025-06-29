import face_recognition
import os
from app import config

def load_known_faces(directory=config.KNOWN_FACES_DIR):
    encodings, names = [], []
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        image = face_recognition.load_image_file(path)
        face_enc = face_recognition.face_encodings(image)
        if face_enc:
            encodings.append(face_enc[0])
            names.append(os.path.splitext(filename)[0])
    return encodings, names

def recognize_faces(frame, known_encodings, known_names):
    rgb = frame[:, :, ::-1]  # BGR to RGB
    locations = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, locations)

    results = []
    for encoding, location in zip(encodings, locations):
        matches = face_recognition.compare_faces(known_encodings, encoding)
        name = "Unknown"
        if matches:
            distances = face_recognition.face_distance(known_encodings, encoding)
            best_match = distances.argmin()
            if matches[best_match]:
                name = known_names[best_match]
        results.append((name, location))
    return results
