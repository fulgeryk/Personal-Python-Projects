# 🎨 Dominant Colors Extractor (Flask + NumPy)

A simple web application that allows users to upload an image and extracts the **Top 5 dominant colors** using **NumPy-based image processing**.

Built from scratch with **Flask**, **Pillow**, and **NumPy**, focusing on understanding image data at pixel level.

---

## 🚀 Features

* 📤 Upload image from your computer
* 🧠 Extract dominant colors using custom algorithm (no external color libraries)
* 🎨 Visual color palette display
* 📊 Pixel count for each dominant color
* ⚡ Fast processing using NumPy
* 🌐 Simple web interface using Flask and Bootstrap

---

## 🖼️ Demo

After uploading an image, the app displays:

* Top 10 dominant colors
* Color preview squares
* RGB values
* Pixel frequency

Example output:

```
rgb(0, 0, 0)     — 165881 px
rgb(16, 16, 16)  — 56766 px
rgb(32, 32, 32)  — 48177 px
...
```

---

## 📸 Screenshot

![DominantColors.png](newimg.png)

## 🧠 How It Works

The algorithm:

1. Loads image using Pillow
2. Converts image to NumPy array
3. Reshapes into list of pixels `(N, 3)`
4. Applies color grouping (quantization)
5. Counts frequency using dictionary
6. Extracts Top 10 dominant colors
7. Sends results to Flask template

This approach provides **full control over image processing logic**.

---

## 🛠️ Tech Stack

* Python 3
* Flask
* NumPy
* Pillow (PIL)
* HTML / CSS
* Bootstrap

---

## 📁 Project Structure

```
project/
│
├── app.py
├── process_image.py
│
├── templates/
│   └── index.html
│
└── README.md
```

## 📚 What I Learned

This project helped me understand:

* How images are represented as arrays
* RGB color space
* NumPy array manipulation
* Flask file upload handling
* Backend → frontend data flow
* Building real projects without tutorials

---

## 🔮 Future Improvements

* Export palette
* Show percentage instead of pixel count
* Download palette image
* Drag & drop upload
* K-Means color clustering

---

## 👨‍💻 Author

- Sorin Fulger

