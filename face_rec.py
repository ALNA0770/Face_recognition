import face_recognition
import cv2
import os 

#Import needed libraries 

# Here we load an image of the person to recognize (your image)
known_image = face_recognition.load_image_file("your_image.jpg")
known_face_encoding = face_recognition.face_encodings(known_image)[0]  # We should use first encoding

# Initialize some variables
face_locations = []
face_encodings = []

folder_path = r"/path/"  # Change this to the folder you want to open

# Open the webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame to match
    ret, frame = video_capture.read()

    # Find all face locations in the frame
    face_locations = face_recognition.face_locations(frame)
    # Get face encodings for any detected faces
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    #  Check if one of them matches the known face or not
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces([known_face_encoding], face_encoding)
        
        if True in matches:
            # If a match is found, do something (We can wite our own command to execute )
            print("Face matched!")
            os.startfile(folder_path)
            


    # Display the result
    cv2.imshow("Video", frame)

    # it will be played until you press 'q' 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Get the video capture and close windows
video_capture.release()
cv2.destroyAllWindows()
