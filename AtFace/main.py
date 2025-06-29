import cv2
from app import face_recognition, camera, attendance

def main():
    known_encodings, known_names = face_recognition.load_known_faces()
    recorded = set()
    video = camera.capture_video()

    while True:
        ret, frame = video.read()
        if not ret:
            break

        results = face_recognition.recognize_faces(frame, known_encodings, known_names)

        for name, _ in results:
            attendance.mark_attendance(name, recorded)

        camera.draw_faces(frame, results)
        cv2.imshow("Face Attendance", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
