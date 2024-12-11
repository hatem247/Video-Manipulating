import cv2
video = cv2.VideoCapture('vid.mp4')
while True:
    ret, frame = video.read()
    if not ret:
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
    frame[:, :, 0] = cv2.equalizeHist(frame[:, :, 0])
    frame = cv2.cvtColor(frame, cv2.COLOR_YUV2BGR)
    cv2.imshow('Vid', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break