import cv2 
import mediapipe as mp
import math 
import numpy as np
from pycaw.pycaw import AudioUtilities

cap = cv2.VideoCapture(0)

thumb_x = 0
thumb_y = 0

index_x = 0
index_y = 0

mpHands = mp.solutions.hands
hands = mpHands.Hands()

mpDraw = mp.solutions.drawing_utils

device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume
minVol, maxVol, _ = volume.GetVolumeRange()
print(minVol, maxVol)

while True:

    success, img = cap.read()

    imgRGB = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2RGB
    )

    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:

        for handLms in results.multi_hand_landmarks:

            for id, lm in enumerate(handLms.landmark):

                if id == 4:

                    h, w, c = img.shape

                    thumb_x = int(lm.x * w)
                    thumb_y = int(lm.y * h)
                    cv2.circle(
                    img,
                    (thumb_x, thumb_y),
                    15,
                    (0,255,0),
                    -1
                    )

                    #print("Thumb:", cx, cy)

                if id == 8:

                    h, w, c = img.shape

                    index_x = int(lm.x * w)
                    index_y = int(lm.y * h)

                    #print("Index:", cx, cy)

                    cv2.circle(
                    img,
                    (index_x, index_y),
                    15,
                    (0,255,0),
                    -1
                    )

                cv2.line(
                img,
                (thumb_x, thumb_y),
                (index_x, index_y),
                (255,0,0),
                3
                )

                length = math.hypot(
                index_x - thumb_x,
                index_y - thumb_y
                )

                #print(length)

                vol = np.interp(
                    length,
                    [30, 200],
                    [minVol, maxVol]
                )

                volume.SetMasterVolumeLevel(
                    vol,
                    None
                )

                volume_percent = np.interp(
                    length,
                    [30, 200],
                    [0, 100]
                )

                '''if length < 35:
                cv2.circle(
                img,
                midpoint,
                15,
                (0,255,0),
                -1
                ) '''

                cv2.putText(
                    img,
                    str(int(length)),
                    (50,50),
                    cv2.FONT_HERSHEY_COMPLEX,
                    1,
                    (255,0,255),
                    3
                )

                cv2.putText(
                    img,
                    f'volume: {int(volume_percent)}%',
                    (50,100),
                    cv2.FONT_HERSHEY_COMPLEX,
                    1,
                    (0,255,0),
                    3
                )

            mpDraw.draw_landmarks(
            img,
            handLms,
            mpHands.HAND_CONNECTIONS
            )

    cv2.imshow("Hand Tracking", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()