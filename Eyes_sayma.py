import cv2
import dlib

# dlib kütüphanesi kur

detecter = dlib.get_frontal_face_detector()
model = dlib.shape_predictor()  # parantez içine yaz 

cap = cv2.VideoCapture(1)

while True:
    _,frame=cap.read()
    dri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


    cv2.imshow("sayma",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

