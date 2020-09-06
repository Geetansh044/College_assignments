import numpy as np
import cv2
import os
import sys

if len(sys.argv) != 3:
    print('Arguments not equal 3')
    check = False

else:
    video_name = sys.argv[1]
    ratio = int(sys.argv[2])
    check = True

def create(video_name, ratio):

    video_path = os.path.abspath(video_name)
    name = video_name.split('.')[0]
    extension = video_name.split('.')[-1]

    try:
        cap = cv2.VideoCapture(video_path)
    except:
        print('Format not supported')
        return


    _ , frame = cap.read()

    FPS= 20.0
    width = int(frame.shape[1] * ratio / 100)
    height = int(frame.shape[0] * ratio / 100)
    FrameSize = (width, height)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')

    out = cv2.VideoWriter(str(name) + '_ouput.' + str(extension), fourcc, FPS, FrameSize)

    while(cap.isOpened()):
        ret, frame = cap.read()

        if ret != True: break

        img = cv2.resize(frame, FrameSize)
        frame = img
        
        cv2.imshow('frame', frame)
        out.write(frame)

        cv2.waitKey(1)

    cap.release()
    out.release()
    cv2.destroyAllWindows()



if check and os.path.exists(video_name):
    create(video_name, ratio)

else:
    print("Video path don't exist")