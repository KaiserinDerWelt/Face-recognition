import cv2
face_cascade = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml')
if face_cascade.empty(): raise Exception("¿es la ruta correcta?")
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
if eye_cascade.empty(): raise Exception("¿es la ruta correcta?")
video = cv2.VideoCapture(0)
while video.isOpened():
    ret, frame = video.read()
    if frame is not None:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
