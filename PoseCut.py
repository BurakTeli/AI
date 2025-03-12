import cv2
import time
import mediapipe as mp

mpPose = mp.solutions.pose
pose = mpPose.Pose()

mpDraw = mp.solutions.drawing_utils

#cap = cv2.VideoCapture("Poz3.mp4")
cap = cv2.VideoCapture(0)


while True:
    success , img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(img)
    print(results.pose_landmarks)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)


        # İstediğim noktaları anlamak için
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, _ = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)

            if id == 13:
                cv2.circle(img, (cx, cy), 5, (255,0,0),cv2.FILLED)

            if id == 14:
                cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)



    cv2.imshow("img", img)
    cv2.waitKey(10)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()