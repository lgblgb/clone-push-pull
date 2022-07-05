import cv2
import os
#把视频逐帧转换成图片     by XTX
def save_img():
    video_path = r'D:/pig_datas/9.15--9.18/00test/'#11待转视频的路径，不需要具体视频文件名，不过这里注意：视频格式为常见格式“mp4”，“avi” ；要使用“/”，by XTX
    videos = os.listdir(video_path)
    for video_name in videos:
        file_name = video_name.split('.')[0]
        folder_name = video_path + file_name
        os.makedirs(folder_name,exist_ok=True)
        vc = cv2.VideoCapture(video_path+video_name) #读入视频文件   by XTX
        i=0
        c=0
        temp = 10 #设置帧间隔获取截取图片数量：temp = 4时，也就是每间隔4帧截取一张图片
        rval=vc.isOpened()
        while rval:   #循环读取视频帧   by XTX
            c = c + 1
            # str(n).zfill(5)
            rval, frame = vc.read()
            pic_path = folder_name+'/'
            if (c % temp == 0):
                if rval:
                    i=i+1
                    cv2.imwrite(pic_path + str(i).zfill(5) + '.jpg', frame)#str(n).zfill(5)设置保存图片文件名格式（5位）00001~    by XTX
                    cv2.waitKey(1)
                else:
                    rval=rval
                    #break
        vc.release()
        print('save_success')
        print(folder_name)
save_img()
