import cv2

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    _, thresh = cv2.threshold(blur, 10, 200, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Konturları alanlarına göre sırala (büyükten küçüğe)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    # İlk konturu al (en büyük kontur)
    if contours:
        main_contour = contours[0]
        area = cv2.contourArea(main_contour)

        # Belirli bir alanın altındaki konturları filtrele
        if area > 100:
            x, y, w, h = cv2.boundingRect(main_contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Kordinat takip etme dikey çizgi
            cv2.line(frame, (x + int(w/2), 0), (x + int(w/2), frame.shape[0]), (255, 0, 0), 2)

            # Kordinat takip etme yatay çizgi için
            cv2.line(frame, (0, y + int(h/2)), (frame.shape[1], y + int(h/2)), (0, 255, 0), 2)

    cv2.imshow("Göz", frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
