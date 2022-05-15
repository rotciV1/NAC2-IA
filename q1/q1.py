# -*- coding: utf-8 -*-

from ast import match_case
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture("q1.mp4")

rm = input('Insira seu RM (Apenas números): ')
rmStr = [int(i) for i in str(rm)]
rmSum = rmStr[0] + rmStr[1] + rmStr[2] + rmStr[3] + rmStr[4]
cardPicker = {
    "Rei Espadas": (1, 2),
    "Rei Ouros": (3, 4),
    "As Ouros": (5, 6),
    "7 Ouros": (7, 8),
    "10 Espadas": (9, 0)
}

rm_Int2Str = repr(rmSum)
lastDigitRm = rm_Int2Str[-1]
card = list(cardPicker.keys())[
    list(cardPicker.values()).index(int(lastDigitRm))]

while True:
    ret, frame = cap.read()

    if not ret:
        break

    match card:
        case "Rei Espadas":
            template = cv2.imread("reiEspadas.png", 0)
            imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            res = cv2.matchTemplate(imgGray, template, cv2.TM_SQDIFF)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

            larg, alt = template.shape[::-1]
            bottom_right = (min_loc[0] + larg, min_loc[1] + alt)
            cv2.rectangle(frame, min_loc, bottom_right, (0, 255, 0), 3)
            cv2.putText(frame, 'CARTA DETECTADA', (50, 50), cv2.FONT_HERSHEY_SIMPLEX,1,(200,50,0),2,cv2.LINE_AA)

        case "Rei Ouros":
            template = cv2.imread("reiOuros.png", 0)
            imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            res = cv2.matchTemplate(imgGray, template, cv2.TM_SQDIFF)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

            larg, alt = template.shape[::-1]
            bottom_right = (min_loc[0] + larg, min_loc[1] + alt)
            cv2.rectangle(frame, min_loc, bottom_right, (0, 255, 0), 3)
            cv2.putText(frame, 'CARTA DETECTADA', (50, 50), cv2.FONT_HERSHEY_SIMPLEX,1,(200,50,0),2,cv2.LINE_AA)

        case "As Ouros":
            template = cv2.imread("asOuros.png", 0)
            imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            res = cv2.matchTemplate(imgGray, template, cv2.TM_SQDIFF)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

            larg, alt = template.shape[::-1]
            bottom_right = (min_loc[0] + larg, min_loc[1] + alt)
            cv2.rectangle(frame, min_loc, bottom_right, (0, 255, 0), 3)
            cv2.putText(frame, 'CARTA DETECTADA', (50, 50), cv2.FONT_HERSHEY_SIMPLEX,1,(200,50,0),2,cv2.LINE_AA)

        case "7 Ouros":
            template = cv2.imread("7Ouros.png", 0)
            imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            res = cv2.matchTemplate(imgGray, template, cv2.TM_SQDIFF)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

            larg, alt = template.shape[::-1]
            bottom_right = (min_loc[0] + larg, min_loc[1] + alt)
            cv2.rectangle(frame, min_loc, bottom_right, (0, 255, 0), 3)
            cv2.putText(frame, 'CARTA DETECTADA', (50, 50), cv2.FONT_HERSHEY_SIMPLEX,1,(200,50,0),2,cv2.LINE_AA)

        case "10 Espadas":
            template = cv2.imread("10Espadas.png", 0)
            imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            res = cv2.matchTemplate(imgGray, template, cv2.TM_SQDIFF)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            

            larg, alt = template.shape[::-1]
            bottom_right = (min_loc[0] + larg, min_loc[1] + alt)
            cv2.rectangle(frame, min_loc, bottom_right, (0, 255, 0), 3)
            cv2.putText(frame, 'CARTA DETECTADA', (50, 50), cv2.FONT_HERSHEY_SIMPLEX,1,(200,50,0),2,cv2.LINE_AA)

    # Exibe resultado
    cv2.imshow("Feed", frame)

    # Wait for key 'ESC' to quit
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

# That's how you exit
cap.release()
cv2.destroyAllWindows()
