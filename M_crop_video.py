import cv2
import os

def extract_frames(video_path):
    # 创建输出目录
    output_dir = os.path.dirname(video_path)
    output_dir = os.path.join(output_dir, "frames")
    os.makedirs(output_dir, exist_ok=True)
    
    # 打开视频文件
    video = cv2.VideoCapture(video_path)
    frame_count = 0
    
    # 逐帧截取图像并保存为PNG
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        
        # 生成文件名并保存图像
        frame_name = f"frame_81792000{frame_count:04d}.png"
        frame_path = os.path.join(output_dir, frame_name)
        cv2.imwrite(frame_path, frame)
        
        frame_count += 1
    
    # 释放资源
    video.release()

    print(f"成功截取并保存了 {frame_count} 帧图像到 {output_dir}")

if __name__ == "__main__":
    video_path = "E:/fan_video/sentry_src_484.avi"
    extract_frames(video_path)
