# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:48:22 2024

@author: w
"""

import yt_dlp

url = "https://mistia.s3.cn-north-1.amazonaws.com.cn/2023-12-16/a12vmqyxwd/1080p.mp4?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIATIV24B6Z6MW4V7BD%2F20240314%2Fcn-north-1%2Fs3%2Faws4_request&X-Amz-Date=20240314T104552Z&X-Amz-SignedHeaders=host&X-Amz-Expires=601200&X-Amz-Signature=f8ae47da34b77f9a3ba99db1c955e2eea8f1dab862eb8008453e30d0619148cb"
url360 = "https://mistia.s3.cn-north-1.amazonaws.com.cn/2023-12-16/a12vmqyxwd/360p.mp4?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIATIV24B6Z6MW4V7BD%2F20240314%2Fcn-north-1%2Fs3%2Faws4_request&X-Amz-Date=20240314T104552Z&X-Amz-SignedHeaders=host&X-Amz-Expires=601200&X-Amz-Signature=f7a405fab8ebb3514f49e5c1fc8664bd87a7603a427c6350af102e04f1c42706"
urlx = "https://twitter.com/i/status/1284421499915403264"
options = {
    
    'outtmpl': r'C:\Users\w\Downloads\videoX.mp4'
    
    }

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([urlx])
    

#%% 影片分段

from moviepy.editor import VideoFileClip
import math

def split_video(video_path, segment_length):
    """
    分割視頻文件。
    
    參數:
    - video_path: 視頻文件的路徑。
    - segment_length: 分割長度，單位為秒。
    """
    # 加載視頻
    clip = VideoFileClip(video_path)
    
    # 計算視頻總時長
    total_duration = clip.duration  # 獲取視頻時長，單位為秒
    
    # 計算需要分割成多少個文件
    segments = math.ceil(total_duration / segment_length)
    
    for i in range(segments):
        # 計算每段視頻的開始和結束時間
        start_time = i * segment_length
        end_time = min((i + 1) * segment_length, total_duration)
        
        # 分割視頻
        new_clip = clip.subclip(start_time, end_time)
        
        # 保存分割後的視頻
        new_clip.write_videofile(f"{video_path}_segment_{i+1}.mp4", codec="libx264", audio_codec="aac")
        
        print(f"Segment {i+1} saved.")
        
    # 釋放資源
    clip.close()

# 使用範例
video_path = r"C:\Users\w\Downloads\video360.mp4"  # 替換成你的視頻文件路徑
split_video(video_path, segment_length=180)  # 每3分鐘分割一次