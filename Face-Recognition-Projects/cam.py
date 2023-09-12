import cv2

cap = cv2.VideoCapture(0)

while True:
    # Read the video stream from the webcam
    ret, frame = cap.read()

    # Perform face recognition or other image processing on the frame
    # ...

    # Display the resulting frame
    cv2.imshow('Webcam', frame)

    # Check for key press event
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the windows
cap.release()
cv2.destroyAllWindows()
