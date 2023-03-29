import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()


while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        start_point = (x, y)
        end_point = (x+w, y+h)
        rgb_color = (0, 255, 0)
        thickness = 3
        cv.rectangle(frame, start_point, end_point, rgb_color, thickness)

    cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()