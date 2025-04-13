# Сначала - pip install opencv-python, чтобы установить библиотеку

import cv2
import numpy as np

# Загрузка каскада для распознавания лиц
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Запуск видеопотока с камеры
cap = cv2.VideoCapture(0)

def determine_color_type(face_image):
    # Преобразуем изображение в цветовое пространство LAB
    lab_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2LAB)
    l_channel, a_channel, b_channel = cv2.split(lab_image)

    # Находим средние значения каналов
    avg_a = np.mean(a_channel)
    avg_b = np.mean(b_channel)

    # Определяем цветотип на основе значений a и b
    if avg_a < -10 and avg_b < -10:
        return "Your color type is winter"
    elif avg_a > 10 and avg_b < -10:
        return "Your color type is summer"
    elif avg_a < -10 and avg_b > 10:
        return "Your color type is autumn"
    elif avg_a > 10 and avg_b > 10:
        return "Your color type is spring"
    else:
        return "I can't determine the color type"

while True:
    # Чтение кадра из видеопотока
    ret, frame = cap.read()
    if not ret:
        break

    # Преобразование кадра в оттенки серого
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Обнаружение лиц на кадре
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Если лица обнаружены, показываем цветотип
    for (x, y, w, h) in faces:
        face_image = frame[y:y+h, x:x+w]
        color_type = determine_color_type(face_image)
        cv2.putText(frame, color_type, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Отображение кадра с сообщением
    cv2.imshow('Video', frame)

    # Проверка нажатия клавиши 'q' или закрытие окна
    key = cv2.waitKey(1)
    
    # Если нажата клавиша 'q', выходим из цикла
    if key == ord('q') or cv2.getWindowProperty('Video', cv2.WND_PROP_VISIBLE) < 1:
        break

# Освобождение ресурсов
cap.release()
cv2.destroyAllWindows()