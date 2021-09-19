import cv2, time
#creating an object, passing zero for external camera

video=cv2.VideoCapture(0)

a=0
while True:

    #create a frame object
    check, frame=video.read()

    print(check)
    print(frame)  #representing image

    #conerting to grayscale
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #show the frame
    cv2.imshow("capturing", gray)

    #press any key to out(milliseconds)
    cv2.waitKey(0)

    #for playing
    key=cv2.waitKey(1)

    if key==ord('q'):
        break


#shutdown the camera
video.release()


