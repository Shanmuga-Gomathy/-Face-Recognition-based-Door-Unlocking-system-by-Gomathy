# -Face-Recognition-based-Door-Unlocking-system-by-Gomathy

# 🚪 Face Detection-Based Door Unlocking System – Data Collection

This Python project collects face images using OpenCV's Haar Cascade to build a dataset for a door unlocking system based on facial recognition. It captures 50 face samples from a webcam and saves them to a local directory.

---

## 🔍 Features

- Captures faces from webcam in real-time
- Detects and extracts face region using Haar Cascade
- Saves grayscale, resized face images (130x100)
- Visual feedback using matplotlib
- Adaptable folder structure (works on any OS)

---

## 📁 File Structure

.
├── collect_faces.py         # This script
├── haarcascade_frontalface_default.xml
└── datasets/
    └── <your_name>/
        ├── 1.png
        ├── 2.png
        └── ...

---

## 🚀 How to Use

1. Install dependencies:
   pip install opencv-python matplotlib ipython

2. Download Haar Cascade:
   - File: haarcascade_frontalface_default.xml  
   - From: https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

3. Run the script:
   python collect_faces.py

4. What happens:
   - It opens your webcam
   - Detects your face
   - Saves 50 images into datasets/<your_name>/

---

## ✏️ Configuration

To use your own name or label:
sub_data = os.path.join('datasets', 'your_name')

No hardcoded Windows paths – everything now uses dynamic path handling (os.path.join) for cross-platform compatibility.

---

## 📸 Preview

Each captured image is shown in real time with bounding boxes and updates automatically with matplotlib.

---

## 🧠 Next Steps

This data can now be used to:
- Train a face recognizer (e.g., LBPH, Eigenfaces, etc.)
- Implement door unlocking logic
- Use with Raspberry Pi or Arduino for hardware control

---

## 📄 License

MIT License – free to use and modify.
