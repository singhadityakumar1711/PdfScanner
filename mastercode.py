-------------CODE--------------

import cv2  # importing open-cv
import os  # importing os module used for interacting with operating system
from PIL import Image  # importing the Image module from the PIL library
from random import randint  # importing the randint module from random library

rand_num1 = randint(0, 500)
rand_num2 = randint(501, 1000)
rand_num = rand_num1 * rand_num2
print(rand_num)


def mouse_click(event, x, y, flags, param):     # function to implement the mouse click event
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        out_text = '(' + str(x) + ',' + str(y) + ')'
        cv2.putText(frame, out_text, (x, y), font, 0.5, (0, 255, 255), 1)
        cv2.imshow('Scanned photo', frame)
        coordinate_list.append(y)
        coordinate_list.append(x)


url = "http://192.168.206.177:8080/video"
cap = cv2.VideoCapture(url)
ret = True
f1 = 0
i = 0
im = []
imv = []
new_frame_rotate = 0
coordinate_list = []
directory = r'D:\PYTHON SCANNED PHOTOS\IMAGE_FOLDER' + str(rand_num)
os.mkdir(directory)
while ret:
    coordinate_list = []
    ret, frame = cap.read()
    if f1 == 0:
        print("PRESS 's' TO SCAN THE DOCUMENT")
        print("PRESS 'q' TO QUIT")
        f1 = f1 + 1
    k = cv2.waitKey(1) & 0xFF  # waits for input from the keyboard
    cv2.imshow("Camera feed", frame)

    if k == ord('s'):
        cv2.destroyWindow("Camera feed")
        cv2.imshow("Scanned photo", frame)
        print("--------------------------------------------")
        print("PRESS 'y' TO CROP THE IMAGE, ELSE PRESS 'n' ")
        p = cv2.waitKey(0)
        if p == ord('y'):
            print("---------------------------------------------------------------------------------------")
            print("THE IMAGE WILL BE CROPPED BASED ON THE TOP-LEFT AND BOTTOM-RIGHT COORDINATES")
            print("TAP ON THE IMAGE TWICE TO SELECT THE TOP-LEFT AND BOTTOM-RIGHT COORDINATES RESPECTIVELY")
            print("---------------------------------------------------------------------------------------")
            cv2.setMouseCallback('Scanned photo', mouse_click)
            print("PRESS ANY KEY IF CROPPING IS DONE")
            print("---------------------------------")
            z = cv2.waitKey(0) & 0xFF
        elif p == ord('n'):
            coordinate_list.append(0)
            print("---------------------------------------------")
        print("PRESS 'u' IF THE IMAGE IS UNREADABLE")
        print("PRESS 'b' TO CONVERT THE IMAGE TO B&W COLOUR")
        k1 = cv2.waitKey(0) & 0xFF
        print("-------------------------------------------------")
        print("PRESS 1 TO ROTATE IMAGE 90* CLOCKWISE")
        print("PRESS 2 TO ROTATE IMAGE 180* ")
        print("PRESS 3 TO ROTATE IMAGE 90* ANTI-CLOCKWISE")
        print("PRESS 4 TO SKIP ORIENTATION SETTINGS")
        print("---------------------------------")
        if k1 == ord('u'):
            if coordinate_list[0] == 0:
                new_frame = frame
            else:
                new_frame = frame[coordinate_list[0]:coordinate_list[2], coordinate_list[1]:coordinate_list[3]]
            k2 = cv2.waitKey(0) & 0xFF
            if k2 == ord('1'):
                new_frame_rotate = cv2.rotate(new_frame, 0)
            elif k2 == ord('2'):
                new_frame_rotate = cv2.rotate(new_frame, 1)
            elif k2 == ord('3'):
                new_frame_rotate = cv2.rotate(new_frame, 2)
            elif k2 == ord('4'):
                new_frame_rotate = new_frame
            cv2.destroyWindow('Scanned photo')
            gray = cv2.cvtColor(new_frame_rotate, cv2.COLOR_RGB2GRAY)
            new = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 10)
            img_path = directory + r'\Scanned' + str(i) + '.jpg'
            cv2.imwrite(img_path, new)
            i = i + 1
            print("PRESS 's' TO SCAN MORE DOCUMENT")
            print("PRESS 'q' TO QUIT")
            continue
        elif k1 == ord('b'):
            if coordinate_list[0] == 0:
                new_frame = frame
            else:
                new_frame = frame[coordinate_list[0]:coordinate_list[2], coordinate_list[1]:coordinate_list[3]]
            k2 = cv2.waitKey(0) & 0xFF
            if k2 == ord('1'):
                new_frame_rotate = cv2.rotate(new_frame, 0)
            elif k2 == ord('2'):
                new_frame_rotate = cv2.rotate(new_frame, 1)
            elif k2 == ord('3'):
                new_frame_rotate = cv2.rotate(new_frame, 2)
            elif k2 == ord('4'):
                new_frame_rotate = new_frame
            cv2.destroyWindow('Scanned photo')
            gray = cv2.cvtColor(new_frame_rotate, cv2.COLOR_RGB2GRAY)
            cv2.imwrite("D://PYTHON SCANNED PHOTOS//Scanned%d.jpg" % i, gray)
            i = i + 1
            print("PRESS 's' TO SCAN MORE DOCUMENT")
            print("PRESS 'q' TO QUIT")
            continue

    elif k == ord('q'):
        ret = False
        break

cv2.destroyAllWindows()
r = 0
image_list = os.listdir(directory)      # block of code to covert the images in pdf format using Pillow package
for img in image_list:
    path = directory + '//' + img
    im.append(0)
    im[r] = Image.open(path)
    r += 1
imv = im.pop(0)
pdf_name = r'D:\PYTHON SCANNED PDFs\MY_PDF' + str(rand_num) + '.pdf'
imv.save(pdf_name, save_all=True, append_images=im)
