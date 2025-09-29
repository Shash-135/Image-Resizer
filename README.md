# Simple Image Resizer using Python

This is a lightweight, command-line Python script that allows you to quickly resize any image to your preferred dimensions. The script uses the OpenCV library to handle image processing efficiently.

## 🚀 Features

-   **Simple Interface:** Easy-to-use command-line interface.
-   **Custom Dimensions:** Prompts the user to enter the desired width and height.
-   **Efficient Processing:** Utilizes OpenCV for fast and reliable image resizing.
-   **Supports Multiple Formats:** Works with common image formats like JPG, PNG, etc.

---

## 🛠️ Technologies Used

-   **Python 3**
-   **OpenCV (cv2):** The core library used for reading, resizing, and writing the image.

---

## ⚙️ How to Use

Follow these steps to resize an image.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/shash-135/Image-Resizer-Python.git](https://github.com/shash-135/Image-Resizer-Python.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd Image-Resizer-Python
    ```
3.  **Place your image:**
    -   Add the image you want to resize into the project directory. For this example, let's assume the image is named `test.jpg`.

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Run the script:**
    ```bash
    python main.py
    ```
6.  **Enter your dimensions:**
    -   The script will prompt you to enter the image filename (e.g., `test.jpg`).
    -   Then, it will ask for the new width and height in pixels.

After execution, a new file named `resized_image.png` will be created in the same directory.
