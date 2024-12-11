import cv2
def reduce_noise_vid(video_path):
    video = cv2.VideoCapture(video_path)
    kernel = (5, 5)
    while True:
        ret, frame = video.read()
        if not ret:
            break
        frame = cv2.GaussianBlur(frame, kernel, 0)
        cv2.imshow('vid', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
def reduce_noise_img(image_path):
    image = cv2.imread(image_path)
    kernel = (5, 5)
    image = cv2.GaussianBlur(image, kernel, 0)
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

reduce_noise_img('img.jpg')
reduce_noise_vid('vid.mp4')