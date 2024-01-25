# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 10:09:48 2024

@author: w
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 示例：创建一个简单的动画
fig, ax = plt.subplots()
x_data = np.linspace(0, 2 * np.pi, 100)
line1, = ax.plot(x_data, np.sin(x_data), label='sin(x)')
line2, = ax.plot(x_data, np.cos(x_data), label='cos(x)')
ax.legend()

def update(frame):
    line1.set_ydata(np.sin(x_data + frame / 10))  # 更新 sin(x) 数据
    line2.set_ydata(np.cos(x_data + frame / 10))  # 更新 cos(x) 数据
    return line1, line2

# 创建动画并指定总帧数
total_frames = 100
animation = FuncAnimation(fig, update, frames=total_frames, interval=100)

# 准备保存视频的参数
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 使用 MP4 编码
video_out = cv2.VideoWriter('output_video_opencv.mp4', fourcc, 10, (640, 480))

# 保存动画为视频文件
for frame_num in range(total_frames):
    plt.close()
    animation.frame_seq = animation.new_frame_seq()  # 重置帧序列
    animation._stop = total_frames - frame_num - 1  # 设置停止帧
    animation._step()  # 更新动画到当前帧
    fig.canvas.draw()
    img = np.array(fig.canvas.renderer.buffer_rgba())
    img_bgr = cv2.cvtColor(img[:, :, :3], cv2.COLOR_RGB2BGR)
    video_out.write(img_bgr)

video_out.release()
