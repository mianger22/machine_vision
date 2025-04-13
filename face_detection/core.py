# Сначала - pip install opencv-python, чтобы установить библиотеку

import cv2

# Загрузка каскада для распознавания лиц
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Запуск видеопотока с камеры
cap = cv2.VideoCapture(0)

while True:
    # Чтение кадра из видеопотока
    ret, frame = cap.read()
    if not ret:
        break

    # Преобразование кадра в оттенки серого
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Обнаружение лиц на кадре
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Если лица обнаружены, показываем сообщение
    if len(faces) > 0:
        cv2.putText(frame, "excellent!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

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