import numpy
from matplotlib import pyplot as plt
import numpy as np
import cv2
import ctypes
import pyautogui
import time
from PIL import Image

user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)


# * MERKEN
# time.sleep(5)
# # {X=685,Y=227,Width=612,Height=605}
# pyautogui.screenshot('my_screenshot.png', region=(685, 227, 612, 605))

# im = Image.open('my_screenshot.png')
# rgb_im = im.convert('RGB')
# r, g, b = rgb_im.getpixel((60, 60))

# if r < 80:
#     opponent = "BLACK"
# * /MERKEN


# button7location = pyautogui.center(
#     pyautogui.locateOnScreen('ref/b_tower.png', region=(31, 28, 59, 56), grayscale=True))
# print(button7location)

# 25 - 35  first row
# 95 - 105 second row
rows = [30, 100, 170, 240, 310, 380, 450, 520]
columns = [35, 105, 175, 245, 310, 380, 455, 525]
chessboard = [
    [[], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], []]]

img_rgb = cv2.imread('my_screenshot.png')
template = cv2.imread('ref/p.png')
w, h = template.shape[:-1]

res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
threshold = .8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):

    if res[pt[1]][pt[0]] < 0.87:
        continue
    print(pt)
    print("SICHIII: " + str(res[pt[1]][pt[0]]))
    for row, val in enumerate(rows):
        if pt[1] - val <= 10:
            for column, val in enumerate(columns):
                if pt[0] - val <= 10:
                    print("Zeile: " + str(row+1) +
                          "; Spalte: " + str(column+1))
                    chessboard[row][column] = "T"
                    break
            break

    # print(pt)
for pt in zip(*loc[::-1]):  # Switch collumns and rows
    if res[pt[1]][pt[0]] < 0.87:
        continue
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imwrite('result.png', img_rgb)

print(chessboard)
