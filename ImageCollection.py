import os
import time
import uuid
import cv2

# Create directories if not exists
os.makedirs("data/images" , exist_ok=True)
os.makedirs("data/labels" , exist_ok=True)

IMAGES_PATH = os.path.join("data" , "images")
no_of_images = 30

# Capture images using webcam
capture = cv2.VideoCapture(0)
for i in range(no_of_images):
    print("Image {} captured...".format(i+1))
    ret , frame = capture.read()
    if ret:
        imgName = os.path.join(IMAGES_PATH, "{}.jpg".format(str(uuid.uuid1())))
        cv2.imwrite(imgName , frame)
        cv2.imshow("frame" , frame)
        time.sleep(0.5)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
capture.release()
cv2.destroyAllWindows()