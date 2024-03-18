# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:48:22 2024

@author: w
"""

import yt_dlp

url = "https://mistia.s3.cn-north-1.amazonaws.com.cn/2023-12-16/a12vmqyxwd/1080p.mp4?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIATIV24B6Z6MW4V7BD%2F20240314%2Fcn-north-1%2Fs3%2Faws4_request&X-Amz-Date=20240314T104552Z&X-Amz-SignedHeaders=host&X-Amz-Expires=601200&X-Amz-Signature=f8ae47da34b77f9a3ba99db1c955e2eea8f1dab862eb8008453e30d0619148cb"
options = {
    
    'outtmpl': r'C:\Users\w\Downloads\video.mp4'
    
    }

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([url])