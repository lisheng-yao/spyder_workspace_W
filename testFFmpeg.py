# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 10:09:48 2024

@author: w
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

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

# 创建动画并指定 FFMpegWriter
animation_writer = FFMpegWriter(fps=10, metadata=dict(artist='Me'), bitrate=1800, extra_args=['-vcodec', 'libx264'])

# 保存动画为视频文件
animation = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=100)
animation.save(r'C:\Users\w\Desktop\output_video.mp4', writer=animation_writer)

plt.show()


#%%

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

# 创建动画
animation = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=100)

# 保存动画为视频文件
animation.save('output_video.mp4', writer='ffmpeg', fps=10) # 请确保已安装 ffmpeg

plt.show()