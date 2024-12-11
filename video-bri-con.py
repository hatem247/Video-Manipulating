import cv2
def adjust_brightness_contrast(frame, contrast, brightness):
    return cv2.convertScaleAbs(frame, alpha=1 - contrast / 127.0, beta=brightness)
video = cv2.VideoCapture('vid.mp4')
while True:
    ret, frame = video.read()
    if not ret:
        break
    frame = adjust_brightness_contrast(frame, contrast=100, brightness=100)
    cv2.imshow('frame', frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
