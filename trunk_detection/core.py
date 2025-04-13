# 1. python -m venv myenv
# 2. myenv\Scripts\activate
# 3. pip install opencv-python mediapipe
# 4. pip install tensorflow
# 5. python core.py

import os
import cv2
import mediapipe as mp

# Настройка уровня логирования TensorFlow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Игнорировать INFO и WARNING сообщения

# Инициализация Mediapipe для распознавания позы
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Инициализация OpenCV для захвата видео
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Преобразование изображения в RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image)

    # Проверка наличия ключевых точек
    if results.pose_landmarks:
        left_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
        right_shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]
        left_hip = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
        right_hip = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP]

        torso_center_x = (left_shoulder.x + right_shoulder.x) / 2
        torso_center_y = (left_shoulder.y + right_shoulder.y) / 2

        if left_hip.visibility > 0.5 and right_hip.visibility > 0.5:
            cv2.putText(frame, 'excellent', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Pose Detection', frame)

    # Проверка нажатия клавиши 'q' или закрытие окна
    if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty('Pose Detection', cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()