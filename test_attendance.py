import cv2
import pandas as pd
from datetime import datetime
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
cap = cv2.VideoCapture(0)
attendance = pd.DataFrame(columns=['Name', 'Time'])

print("Face camera 5 seconds! Green box = MARKED!")
with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
    frame_count = 0
    while frame_count < 150:  # 5 seconds @ 30fps
        ret, frame = cap.read()
        if not ret: break
        
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(rgb_frame)
        
        if results.detections and 'you' not in attendance['Name'].values:
            time = datetime.now().strftime('%H:%M:%S')
            attendance.loc[len(attendance)] = ['you', time]
            print(f"SAVED: you at {time}")
            cv2.putText(frame, "ATTENDANCE MARKED!", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)
        
        # Draw green box
        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                h, w, _ = frame.shape
                x, y = int(bboxC.xmin * w), int(bboxC.ymin * h)
                cv, ch = int(bboxC.width * w), int(bboxC.height * h)
                cv2.rectangle(frame, (x,y), (x+cv,y+ch), (0,255,0), 3)
                cv2.putText(frame, "FACE DETECTED", (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
        
        cv2.imshow('Attendance [Q to quit early]', frame)
        frame_count += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

print(f"Saving {len(attendance)} records...")
attendance.to_csv('attendance/today.csv', index=False)
cap.release()
cv2.destroyAllWindows()
print(" CHECK CSV NOW!")
