from ultralytics import YOLO
import cv2

# Load model YOLO
model = YOLO("models/best.pt")

# Buka kamera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Kamera tidak terbaca")
        break

    # Deteksi objek
    results = model(frame)

    # Tampilkan hasil deteksi
    annotated_frame = results[0].plot()

    cv2.imshow("YOLO Camera", annotated_frame)

    # Tekan Q untuk keluar
    if cv2.waitKey(1) & 0xFF == ord("q"): 
        break

cap.release()
cv2.destroyAllWindows()