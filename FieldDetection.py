import cv2
import pickle
import numpy as np

cap = cv2.VideoCapture("video.mp4")

def check(frame1):
    spacecounter = 0
    for pos in liste:
        x, y = pos

        crop = frame[y:y + 15, x:x + 26]

        # Gri hale
        gray_crop = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)

        # Eşik değerini belirleme
        _, thresholded = cv2.threshold(gray_crop, 100, 255, cv2.THRESH_BINARY)

        # Non-zero piksel sayısını hesaplama
        count = cv2.countNonZero(thresholded)

        if count < 100:
            color = (0, 255, 0)  # Yeşil
            spacecounter+=1
        else:
            color = (0, 0, 255)  # Kırmızı

        cv2.rectangle(frame, pos, (pos[0] + 26, pos[1] + 15), color, 2)

    cv2.putText(frame,f"bos:{spacecounter}/{len(liste)}",(15,24),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
with open("Otopark_algılama", "rb") as f:
    liste = pickle.load(f)



while True:
    _, frame = cap.read()
    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gri, (3, 3), 1)
    thres = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    median = cv2.medianBlur(thres, 5)
    dilates = cv2.dilate(median, np.ones((3, 3)), iterations=1)

    check(dilates)

    cv2.imshow("göster", frame)
    # cv2.imshow("gri", gri)
    # cv2.imshow("median", median)
    # cv2.imshow("thresh", thres)
    # cv2.imshow("blur", blur)

    if cv2.waitKey(200) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


