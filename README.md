# 🧠 Face Recognition Project

This Python project uses face recognition to open a specific folder when a predefined face is detected. The folder remains hidden, and once the correct face is recognized, the folder will be opened.

## 🐾 Features

- **Face Recognition**: Detects and matches a face with a pre-configured known face.
- **Opens Folder**: Once the face matches, the designated folder opens automatically.
- **Webcam Interface**: Uses OpenCV to access the webcam and process images for real-time face recognition.

## Requirements

- Python 3.x
- Virtual Environment (optional, recommended)

### 🗽 Python Libraries

The project uses the following Python libraries:

- `face_recognition`
- `opencv-python`
- `numpy`
- `pillow`
- `dlib`

You can install all the required libraries via the `requirements.txt` file.

## Setup 📘

1. **Clone the repository** or download the project files to your local machine.

2. **Create and activate a virtual environment**:

    On Windows:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

    On Mac/Linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    After activating the virtual environment, run the following command to install the necessary libraries:
    ```bash
    pip install -r requirements.txt
    ```

4. **Prepare the reference face image**:
    - Save your reference image (the face to recognize) in the same directory as the Python script.
    - Rename the file to `your_image.jpg` or change the filename in the script to match your image name.

5. **Configure the folder path**:
    - Set the `folder_path` variable in `face_rec.py` to the location of the folder you want to open.
    - Ensure the folder exists in the specified location.

6. **Run the script**:
    After the setup, run the script using:
    ```bash
    python face_rec.py
    ```

    The webcam will start, and the system will continuously check for a face. If the face matches the stored image, the folder will open.

7. **Exit the script**:
    Press the **'q'** key to stop the webcam and exit the script.

## License ⚖️

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more details.

ALNA (nazarov31ali@gmail.com)
