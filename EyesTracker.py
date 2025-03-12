import cv2


cap = cv2.VideoCapture(1)
#cap = cv2.VideoCapture("SaçmaGöz.MOV")

while True:
    ret, frame = cap.read()
    if ret == False:
        break

    gri = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    Blur = cv2.GaussianBlur(gri,(7,7),0)


    # Renkler en yoğun yerleri alır thresh değeri 10 dur
    _,thresh = cv2.threshold(Blur,10,200,cv2.THRESH_BINARY_INV)


    #findContours => Şekillerin dış sınırları için
    #RETR_TREE => kontrolleri geri alır düzneler
    #CHAIN_APROX_SIMPLE => Kontrol noktaları sıkıştır gereksiz yerleri kaldırır
    contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # Alanalra göre büyükten küçüğe sıralar
    # reverse=False olsaydı küçükten büyüye olurdu
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    #print(contours)




    # Verilen kontorü saran bir dikdörtgen alır
    # her cnt değeri için alır
    for cnt in contours[:1]:
        area = cv2.contourArea(cnt)

        #area = cv2.contourArea(cnt)
        #print(cnt)

        if area>200:
            (x,y,w,h) = cv2.boundingRect(cnt)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        # kordinat takip etme dikey çizgi
            cv2.line(frame,(x+int(w/2),0),(x+int(h/2),frame.shape[0]),(255,0,0),2)

        # kordinat taki etme yatay çizgi için
            cv2.line(frame, (0, y + int(h/2)), (frame.shape[1], y+int(h/2)), (0, 255, 0), 2)


    cv2.imshow("göz",frame)
    #cv2.imshow("göz",thresh)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
