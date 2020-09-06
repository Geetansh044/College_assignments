import numpy as np
import cv2
import os
import sys

if len(sys.argv) != 2:
    print('Arguments not equal 2')
    check = False

else:
    video_name = sys.argv[1]
    check = True

def create(video_name):

    video_path = os.path.abspath(video_name)
    name = video_name.split('.')[0]
    extension = video_name.split('.')[-1]

    try:
        cap = cv2.VideoCapture(video_path)
    except:
        print('Format not supported')
        return

    ret, frame = cap.read()

    FPS= 20.0
    FrameSize=(frame.shape[1], frame.shape[0])
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')

    out = cv2.VideoWriter(str(name) + '_ouput.' + str(extension), fourcc, FPS, FrameSize, 0)

    while(cap.isOpened()):
        ret, frame = cap.read()

        if ret != True: break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = gray

        out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()



if check and os.path.exists(video_name):
    create(video_name)

else:
    print("Video path don't exist")