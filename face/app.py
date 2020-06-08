import base64
import cv2
# import dlib
from gaze_tracking import GazeTracking
from scipy.spatial import distance
gaze = GazeTracking()
frameRate = 20.0


class Face():

    def __init__(self):
        print("Initialized")

    def detect(self, image):
        # image = cv2.imread("images/download.jpeg")
        # image = cv2.resize(image, (560,400), interpolation=cv2.INTER_AREA)

        # im = cv2.imread("newmask.png")

        # cv2.rectangle(image, (400, 300), (700, 500), (178, 190, 181), 5)

        frame = cv2.flip(image, 2)

        gaze.refresh(frame)

        frame, x, y = gaze.annotated_frame()
        text = ""

        # cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

        left_pupil = gaze.pupil_left_coords()

        right_pupil = gaze.pupil_right_coords()
        print(right_pupil, left_pupil)

        points_cnt = (x, y)


        if left_pupil and right_pupil != None:
            a = left_pupil
            b = right_pupil
            c = points_cnt
            # dist = [(a - c) ** 2 for a, c in zip(a, c)]
            # dist = math.sqrt(sum(dist))
            # print("new method",dist)

            dst_left = distance.euclidean(a, c)
            mm = 0.26458333
            dist_left_mm = (dst_left * mm) + 20

            print("left:::", dist_left_mm)
            dst_right = distance.euclidean(b, c)
            # print(dst_right)
            # print(dst_left)

            dist_right_mm = (dst_right * mm) + 20
            total_pd = dist_right_mm + dist_left_mm
            print("total::", total_pd)
            print("right::", dist_right_mm)

            cv2.putText(frame, "Left PD:  " + str(dist_left_mm) + 'mm', (85, 125), cv2.FONT_HERSHEY_DUPLEX, 0.9,
                        (0, 0, 255), 1)
            cv2.putText(frame, "Right PD: " + str(dist_right_mm) + 'mm', (85, 175), cv2.FONT_HERSHEY_DUPLEX, 0.9,
                        (0, 0, 255), 1)
            cv2.putText(frame, "Total PD: " + str(total_pd) + 'mm', (85, 200), cv2.FONT_HERSHEY_DUPLEX, 0.9,
                        (0, 0, 255), 1)

        # im = cv2.resize(im, frame.shape[1::-1], interpolation=cv2.INTER_AREA)
        # dst = cv2.addWeighted(frame, 0.5, im, 0.5, 0)
        # flip = cv2.flip(dst, 1)


        # ret, jpeg = cv2.imencode('.jpg', dst)
        # return jpeg.tobytes()


        image = cv2.imencode('.jpg', frame)[1]
        return base64.b64encode(image).decode('utf-8', 'strict')


