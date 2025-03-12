import cv2
import time

# OpenCV Cascade sınıflandırıcıları
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Webcam başlatma
cap = cv2.VideoCapture(1)

while True:
    start_time = time.time()  # İşlemlerin başlangıç zamanını kaydet

    # Webcam'den bir çerçeve okuma
    ret, frame = cap.read()

    if not ret:
        break

    # Gri tonlamaya çevir
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri tespit et
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Gülümsüyorsa yazdır
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20)
        for (sx, sy, sw, sh) in smiles:
            cv2.putText(frame, "gülümsüyor", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Ekranı göster
    cv2.imshow("Face Detection", frame)

    end_time = time.time()  # İşlemlerin bitiş zamanını kaydet
    elapsed_time = end_time - start_time  # İşlemlerin süresini hesapla
    print(f"Geçen Süre: {elapsed_time} saniye")

    # Çıkış için 'q' tuşuna basma kontrolü
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Webcam kapatma
cap.release()
cv2.destroyAllWindows()
