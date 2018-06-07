from scripts.label_image import label_img
import cv2

# set up
cap = cv2.VideoCapture(1)
cap.set(3, 1920)
cap.set(4, 1080)
cap.set(5, 60)

cv2.namedWindow('SmartScope', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('SmartScope', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
font = cv2.FONT_HERSHEY_SIMPLEX
colour = (255, 64, 16) #BGR

def print_results(string):
    cv2.putText(frame, string, (25, 420), font, 0.75, colour, 1, cv2.LINE_AA)

while(True):
    # capture frame-by-frame
    ret, frame = cap.read()
    
    # processing user input
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        cv2.imwrite('tf_files/img.jpg', frame)
        detected, confidence = label_img()
    elif key == ord('c'):
        detected = ''
    
    # operations on the frame
    cv2.putText(frame,'SmartScope', (0, 25), font, 1, colour, 3, cv2.LINE_AA)

    if (detected != ''):
        print_results(detected + ' detected - confidence: ' + str('%.2f'%(confidence * 100)) + '%')

    cv2.imshow('SmartScope', frame)

# when everything done, release the capture
cap.release()
cv2.destroyAllWindows()
