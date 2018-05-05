import cv2, time
import darknet as dn
from collections import deque

# setting vars
cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)
cap.set(5, 60)
cv2.namedWindow('SmartScope', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('SmartScope', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

path = "/path/to/darknet/"
net = dn.load_net(path + "cfg/yolov3.cfg", path + "yolov3.weights", 0)
meta = dn.load_meta(path + "cfg/coco.data")
dn.set_gpu(0)
q = deque()

fontface = cv2.FONT_HERSHEY_SIMPLEX
colour = (128, 200, 255) #BGR

def rd (x):
    return int(round(x))

while(True):

        # capture frame-by-frame
        ret, frame = cap.read()
        cv2.imwrite('img.jpg', frame)
        #frame = cv2.imread(path + 'data/dog.jpg')

        # computing and displaying output
        results = dn.detect(net, meta, path + "python/img.jpg")

        # displaying objects
        for ob in results:
            print (ob)
            print '\n'
            coord = ob[2]
            coord = rd(coord[0]), rd(coord[1]), rd(coord[2]), rd(coord[3])
            cv2.ellipse(frame, (coord[0], coord[2]),(coord[1], coord[3]), 0, 0,
                        360, (0, 255, 0), 3)
            cv2.putText(frame, ob[0], (coord[0], coord[2]), fontface, .75, colour,
                        1, cv2.LINE_AA)
            q.append((coord[0], coord[2]))
            if len(q) > 6000:
                q.popleft()

        # highlighting trajectory
        for point in q:
            cv2.circle(frame,point, 2, (0,0,255), -1)
        print '\n'

        cv2.putText(frame,'SmartScope', (0, 25), fontface, 1, colour, 3, cv2.LINE_AA)
        cv2.imshow('SmartScope', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        time.sleep(0.01)

# when everything done, release the capture
cap.release()
cv2.destroyAllWindows()
