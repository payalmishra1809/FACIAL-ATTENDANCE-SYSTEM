import cv2
import numpy as np
import os
import pickle
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
known_faces = []
known_names = []

print("Scanning known_faces folder...")
for filename in os.listdir('known_faces/'):
    if filename.endswith('.jpg'):
        image = cv2.imread(f'known_faces/{filename}')
        if image is None:
            print(f"Can't read {filename}")
            continue
            
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        with mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1) as face_mesh:
            results = face_mesh.process(rgb_image)
            if results.multi_face_landmarks:
                landmarks = results.multi_face_landmarks[0].landmark
                face_array = np.array([[lm.x, lm.y, lm.z] for lm in landmarks])
                name = filename.split('_')[0]
                known_faces.append(face_array)
                known_names.append(name)
                print(f"Encoded: {name} from {filename}")
            else:
                print(f"No face detected in {filename}")

print(f"Total faces encoded: {len(known_faces)}")
with open('encodings.pkl', 'wb') as f:
    pickle.dump((known_faces, known_names), f)
print("Encodings saved!")
