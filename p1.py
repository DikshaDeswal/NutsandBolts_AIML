# code to predict
import cv2
import mediapipe as mp

#To predict the face detections enter1
#To predict the hand detections enter2
#To predict the pose detections enter3

def predict_hand_shape():
    mp_draw = mp.solutions.drawing_utils
    mp_hand = mp.solutions.hands

    video = cv2.VideoCapture(0)

    with mp_hand.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
        while True:
            ret, image = video.read()
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = hands.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_draw.draw_landmarks(image, hand_landmarks, mp_hand.HAND_CONNECTIONS)

            cv2.imshow("Frame", image)
            k = cv2.waitKey(1)
            if k == ord('d'):
                break

    video.release()
    cv2.destroyAllWindows()


def predict_face_shape():
    mp_drawing = mp.solutions.drawing_utils
    mp_face_detection = mp.solutions.face_detection

    video = cv2.VideoCapture(0)

    with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
        while True:
            ret, image = video.read()
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = face_detection.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.detections:
                for detection in results.detections:
                    mp_drawing.draw_detection(image, detection)

            cv2.imshow('MediaPipe Face Detection', image)
            k = cv2.waitKey(1)
            if k == ord('d'):
                break

    video.release()
    cv2.destroyAllWindows()


def predict_body_shape():
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_pose = mp.solutions.pose

    video = cv2.VideoCapture(0)

    cap = cv2.VideoCapture(0)
    with mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                continue
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            mp_drawing.draw_landmarks(image,results.pose_landmarks,mp_pose.POSE_CONNECTIONS,
                                      landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
            cv2.imshow('MediaPipe Pose', image)
            k = cv2.waitKey(1)
            if k == ord('d'):
                break
    cap.release()
    cv2.destroyAllWindows()

def main():
    object = int(input("Enter the keyword: "))
    if object == 1:
        predict_hand_shape()
    if object == 2:
        predict_face_shape()
    if object == 3:
        predict_body_shape()


main()
