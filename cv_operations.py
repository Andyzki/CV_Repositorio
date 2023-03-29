import cv2
import os

path = os.getcwd()


def take_photo(name: str):
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        raise 'cannot open camera'
        exit(1)
        
    while True:
        ret, frame = cap.read()

        if not ret:
            raise "can't receive frame (stream end?)"

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) == ord('q'):
            _save_photo(name, frame)
            break

    cap.release()

def _save_photo(name: str, frame):
    dir_photo = os.path.join(path, 'photos', name)
    photo_name = os.path.join(dir_photo, name + '.png')
    if os.path.exists(dir_photo):
        os.mkdir(dir_photo)
    cv2.imwrite(photo_name, frame)