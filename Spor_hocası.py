import time
import cv2
import mediapipe as mp
import math


cap = cv2.VideoCapture("Spor2.mp4")

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils



while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = pose.process(imgRGB)

    lmList = []
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, _ = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            lmList.append([id, cx, cy])
    print(lmList)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imshow("video",img)
    cv2.waitKey(20)
