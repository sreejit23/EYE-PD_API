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

    def detect(self, frame):
        abc = frame
        frame = cv2.flip(frame, 1)

        gaze.refresh(frame)


        blink = gaze.is_blinking()
        # print("@@@2", blink)
        if blink != True:

            frame, x, y = gaze.annotated_frame()


            left_pupil = gaze.pupil_left_coords()

            right_pupil = gaze.pupil_right_coords()
            print(right_pupil, left_pupil)

            points_cnt = (x, y)


            if left_pupil and right_pupil != None:
                a = left_pupil
                b = right_pupil
                c = points_cnt

                dst_left = distance.euclidean(a, c)
                mm = 0.26458333
                dist_left_mm = (dst_left * mm) + 16
                dist_left_mm = round(dist_left_mm,2)

                print("left:::", dist_left_mm)
                dst_right = distance.euclidean(b, c)

                dist_right_mm = (dst_right * mm) + 16
                dist_right_mm = round(dist_right_mm,2)
                total_pd = dist_right_mm + dist_left_mm
                total_pd=round(total_pd,2)
                print("total::", total_pd)
                print("right::", dist_right_mm)

                # frame = cv2.flip(frame, 2)


                cv2.putText(frame, "Left PD:  " + str(dist_left_mm) + 'mm', (300, 25), cv2.FONT_HERSHEY_DUPLEX, 0.9,
                            (0, 0, 255), 1)
                cv2.putText(frame, "Right PD: " + str(dist_right_mm) + 'mm', (300, 55), cv2.FONT_HERSHEY_DUPLEX, 0.9,
                            (0, 0, 255), 1)
                cv2.putText(frame, "Total PD: " + str(total_pd) + 'mm', (300, 85), cv2.FONT_HERSHEY_DUPLEX, 0.9,
                            (0, 0, 255), 1)


            image = cv2.imencode('.jpg', frame)[1]
            return base64.b64encode(image).decode('utf-8', 'strict')

        else:
            image = cv2.imencode('.jpg', abc)[1]
            return base64.b64encode(image).decode('utf-8', 'strict')



