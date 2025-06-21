import cv2
import os
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

# Define file paths using os.path for platform independence
base_dir = os.path.abspath(os.path.dirname(__file__))
haar_file = os.path.join(base_dir, 'haarcascade_frontalface_default.xml')
datasets = os.path.join(base_dir, 'datasets')
person_name = 'elon_musk'  # Change this to any user/label
sub_data = os.path.join(datasets, person_name)

# Ensure the dataset directory exists
os.makedirs(sub_data, exist_ok=True)

(width, height) = (130, 100)
face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0)

count = 1
while count < 51:
    print(f"Capturing image {count}")
    ret, im = webcam.read()

    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        cv2.imwrite(os.path.join(sub_data, f'{count}.png'), face_resize)

    count += 1

    im_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    plt.imshow(im_rgb)
    plt.axis('off')
    clear_output(wait=True)
    display(plt.gcf())

    if cv2.waitKey(10) == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
