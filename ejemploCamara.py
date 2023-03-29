import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()


while True:
    # Capture frame por frame
    ret, frame = cap.read()
    # si el Frame esta correcto ret sera True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Aqui podemos modificar los Frames, de ser necesario
		# en este caso lo pasaremos a una escala de grises
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Mostramos el Frame resultande de la modificacion
    cv.imshow('frame', gray)

		# Asignamos la letra q para salir del programa
    if cv.waitKey(1) == ord('q'):
        break

# Cuando todo este listo empezamos a capturar
cap.release()