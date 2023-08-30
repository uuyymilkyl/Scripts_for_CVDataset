# 脚本：获取图像 from 相机/视频
# 作者：黄敏瑜 uuyymilkyl
# 使用时改掉path即可,建议使用random + time + i 避免重复命名 


import cv2 
import os

path = "E:/3号能量机关视频/image/"

def Getframe():
    cv2.namedWindow('real_img', cv2.WINDOW_NORMAL)
    #cap = cv2.VideoCapture(0)
	cap = cv2.VideoCapture("E:/3/sentry_src_484.avi");
    while(cap.isOpened()):
        ret, frame = cap.read()
        cv2.imshow('real_img', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # 释放画面
    cap.release()
    cv2.destroyAllWindows()
    return frame


if __name__ == "__main__":
    for i in range(500):
        frame = Getframe()
		name = i + "fan"
        cv2.imwrite(path+name,frame)