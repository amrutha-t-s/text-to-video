from moviepy.video.VideoClip import VideoClip, TextClip, ColorClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
import numpy as np
import os

print("🔥 Starting Text-to-Video Generator...")
print("📁 Current folder:", os.getcwd())

def make_frame(t):
    duration = 10
    width, height = 1280, 720
    x = np.interp(t, [0, duration], [width + 100, -800])
    y = height // 2
    
    txt_clip = TextClip(
        text="Your project: AI Text-to-Video Generator!\nBuilt with Python & MoviePy in VSCode",
        font_size=60, 
        color='white'
    ).with_position((x, y)).with_duration(duration)
    
    return txt_clip.get_frame(t)

print("🎨 Creating background...")
bg = ColorClip(size=(1280, 720), color=(50, 100, 200), duration=10)

print("✨ Creating animated text...")
video = CompositeVideoClip([bg, VideoClip(make_frame, duration=10)], size=(1280,720))

print("💾 Saving output.mp4 (20-30 seconds)...")
# FIXED: Removed verbose/logger parameters for MoviePy 2.2.1
video.write_videofile("output.mp4", fps=30, codec='libx264', audio=False)
print("✅ COMPLETE! Check output.mp4")

video.close()
bg.close()
