import cv2
from ultralytics import YOLO

# Baixa e carrega o modelo YOLOv8 Nano (leve e rápido)
model = YOLO("yolov8n.pt")

# Classificador Haar para detecção de rostos (já vem com OpenCV)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 1. Detecção de objetos (80 classes: pessoa, carro, celular, etc.)
    results = model(frame, verbose=False)
    annotated_frame = results[0].plot()

    # 2. Detecção específica de rostos
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(annotated_frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(annotated_frame, "ROSTO", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Reconhecimento em Tempo Real", annotated_frame)

    # Pressione 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
