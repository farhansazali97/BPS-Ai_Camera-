import cv2


cam = cv2.VideoCapture(0)

cv2.namedWindow("ESC to exit", cv2.WINDOW_NORMAL)
cv2.resizeWindow("ESC to exit", 500, 300)

img_counter = 0

while True:
    ret, frame = cam.read()
    
    cv2.imshow("ESC to exit", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
 
cam.release()

cv2.destroyAllWindows()
