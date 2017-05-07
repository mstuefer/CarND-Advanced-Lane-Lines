import cv2

# exporting all frames in a video as jpg images

video = cv2.VideoCapture('challenge_video.mp4')
count = 0
success = True

while success:
    success, image = video.read()
    cv2.imwrite("test_images/cvideo_image%d.jpg" % count, image)
    count += 1
