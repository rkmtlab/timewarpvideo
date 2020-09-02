# テニスで、敵からこちらへの時間だけを遅くして再生してみる。

import cv2
import os

fname = 'tennis.mp4'
slow = 2
# 遅くするフレームの範囲
slow_range = [[45, 74], [110, 139], [173, 216], [254, 284]]


cap = cv2.VideoCapture(fname)

i =0
j = 0
while cap.isOpened():
    if i > 300:
        break
    ret, ff = cap.read()
    frame = ff.copy()

    a = cv2.imwrite('/tmp/video%04d.jpg' % (j,), frame)
    j = j + 1
        
    if True in [x[0] <= i < x[1] for x in slow_range]:
        for k in range(0, slow):
            cv2.imwrite('/tmp/video%04d.jpg' % (j,), frame)
            j = j + 1

    i = i + 1
    
cap.release()

os.system("ffmpeg -r 25 -i /tmp/video%04d.jpg -vcodec libx264 out.mp4")
print("out.mp4 generated")
