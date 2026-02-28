**Digital Safety Mirror**
**AI-Based Real-Time Human Safety Monitoring System**


**📌 Project Description**
The Digital Safety Mirror is an AI-based real-time monitoring system designed to detect unsafe human situations such as:

• Fall Detection
• Unsafe Posture
• Imbalance

Traditional surveillance systems focus only on detecting general motion for security purposes. However, they fail to identify safety-related human risks such as falling, improper posture, or imbalance.

This project improves upon existing motion detection systems by incorporating Human Pose Detection using AI techniques to monitor the user continuously and generate alerts when unsafe situations are detected.

The system uses a webcam to capture live video, processes the video using MediaPipe Pose Detection, and displays real-time alerts through a Streamlit-based smart mirror interface.

**🎯 Objectives**
• To monitor human activity in real-time

• To detect unsafe posture and imbalance

• To identify fall situations

• To generate instant alerts for safety risks

• To provide a user-friendly smart mirror interface

**✔  Technologies Used**
Technology                    Purpose
• Python	                  Programming Language
• OpenCV	                  Video Capture & Processing
• MediaPipe	                  Human Pose Detection
• NumPy	                      Numerical Calculations
• Streamlit	                  Frontend Interface
• VS Code	                  Development Environment


**✔  Functional Requirements**
• Capture real-time video using webcam

• Detect human body landmarks

• Analyze posture and body alignment

• Detect fall or imbalance

• Generate alert messages

• Display real-time monitoring dashboard

**✔  Non-Functional Requirements**
• Real-time system performance

• Detection accuracy ≥ 80%

• User-friendly interface

• Low cost implementation

• Reliable alert generation


**✔  Working Process**
1.Webcam captures live video feed.

2.Video frames are processed using OpenCV.

3.MediaPipe extracts body landmarks from frames.

4.System calculates:

   • Body height
   • Shoulder alignment
   • Head position

5.Safety detection logic identifies:

   • Fall
   • Unsafe posture
   • Imbalance

6.Alert message is generated if unsafe condition is detected.

7.Streamlit dashboard displays:

   • Live video feed
   • Alert message
   • System status
   • FPS counter
   • Detection accuracy

**📁 Project Folder Structure**
digital-safety-mirror/
│
├── app.py
├── pose_detector.py
├── safety_detection.py
├── alert.py
├── requirements.txt
└── README.md

**✔ File Description**
**🔹 app.py**
• Streamlit Frontend

• Camera access

• FPS Counter

• Accuracy Dashboard

• Alert Display

**🔹 pose_detector.py**
• Uses MediaPipe Pose

• Detects body landmarks

• Returns pose data

**🔹 safety_detection.py**
• Fall detection logic

• Posture analysis

• Imbalance detection

**🔹 alert.py**
• Displays alert message

• Shows warning on screen

**🔹 requirements.txt**
• Contains required libraries for project execution.

**✔  Expected Output**
•Live video monitoring

•Detection of unsafe posture

•Fall detection alert

•Imbalance detection alert

•Real-time FPS display

•Detection accuracy dashboard

**✔  Applications:**
•Elderly care monitoring

•Workplace safety

•Hospital patient monitoring

•Smart home systems

•Rehabilitation centers

**✔  Future Enhancements**
•SMS or Email alert system

•IoT integration

•Mobile application support

•Cloud-based monitoring

•Emergency contact notification

**✔ Conclusion:**
The Digital Safety Mirror provides an efficient and low-cost solution for real-time human safety monitoring. By integrating AI-based pose detection with a smart interface, the system ensures timely detection of unsafe situations and helps in preventing accidents in homes, hospitals, and workplaces.

