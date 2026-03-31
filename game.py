import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import pyautogui as auto

cap = cv2.VideoCapture(0)
hd = HandDetector(maxHands=1)

while True:
    rt, frame = cap.read()
    
    
    frame = cv2.flip(frame, 1) 
    
    frame = cv2.resize(frame, (580, 480))
    cvzone.putTextRect(frame, 'GAME', [360, 40], scale=3, thickness=3, border=2)

    hand, frame = hd.findHands(frame)

    if hand:
        hands = hand[0]
        lmlist = hands['lmList']

        # حساب المسافة بين الإبهام (4) والسبابة (8)
        length, info, frame = hd.findDistance(lmlist[4][0:2], lmlist[8][0:2], frame)
        length = round(length)

        if length < 25:
            auto.press('up')

    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()