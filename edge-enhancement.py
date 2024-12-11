import cv2
import numpy as np
def enhance_edges(video_path):
    video = cv2.VideoCapture(video_path)
    kernel = np.array([
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
    ])
    while True:
        ret, frame = video.read()
        if not ret:
            break
        enhanced_frame = cv2.filter2D(frame, -1, kernel)
        cv2.imshow('Edge Enhancement', enhanced_frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
enhance_edges('vid.mp4')
