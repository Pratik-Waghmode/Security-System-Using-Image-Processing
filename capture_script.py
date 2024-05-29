import cv2

camera = cv2.VideoCapture(0)
for i in range(1):
    return_value, image = camera.read()
    cv2.imwrite('Camera_Capture'+str(i)+'.png', image)
del(camera)