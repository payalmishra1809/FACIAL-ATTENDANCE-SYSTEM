MediaPipe Face Attendance System README
A real-time facial recognition attendance system using MediaPipe landmarks for precise face matching. Encodes known faces from images, recognizes via webcam, and logs attendance to CSV—perfect for classroom or workplace use in your B.Tech computer vision projects.
​

Features
Extracts 468 3D facial landmarks (x,y,z) for robust encoding.

Live multi-face detection with Euclidean distance matching.

Duplicate prevention and timestamped CSV exports.

Simple setup: Drop JPGs in folder, run script.
​

Prerequisites
Python 3.8+ with webcam access.

Install: pip install opencv-python mediapipe numpy.

Quick Setup
Create known_faces/ folder, add 10-20 JPG photos per person (e.g., student1.jpg).

Run training: python encodings.py → Creates encodings.pkl.

Run recognition: python recognize.py (use skeleton from previous response).

View logs in attendance.csv.
​

File Structure
text
project/
├── encodings.py      # Generates face encodings [file:21]
├── recognize.py      # Live webcam attendance (create next)
├── known_faces/      # Training JPGs
├── encodings.pkl     # Saved landmarks + names
└── attendance.csv    # Logs: Name,Time,Date
Usage Example
text
$ python encodings.py
Scanning known_faces folder...
Encoded: you from student1.jpg
Total faces encoded: 1
Encodings saved!

$ python recognize.py
[Live camera starts - marks attendance automatically]
Customization
Names: Edit name = "you" in encodings.py to parse filenames (e.g., name = filename.split('_')[0]).

Threshold: In recognize.py, set distance < 0.5 for "match".

Extend: Add Tkinter GUI, Firebase DB, or ESP32 integration for your IoT projects.
​

Troubleshooting
No detection? Ensure good lighting, frontal faces in training images.

Slow? Reduce max_num_faces=1 or use GPU MediaPipe.

Errors? Verify OpenCV webcam index (0 or 1).
​

License
MIT License - Free for academic/commercial use. Built for your Chennai college projects with VS Code/Python stack.
