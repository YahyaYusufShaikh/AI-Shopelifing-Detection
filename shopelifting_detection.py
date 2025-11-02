from ultralytics import YOLO
import cv2

# Load YOLOv8 pre-trained model
model = YOLO("yolov8n.pt")  # nano model - small & fast

# Load video (you can replace with '0' for webcam)
video_path = "test_video.mp4"
cap = cv2.VideoCapture('demo2.output.mp4')

# Check if video loaded
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform detection
    results = model(frame)

    # Draw results on the frame
    annotated_frame = results[0].plot()

    # Display the output
    cv2.imshow("Shoplifting Detection Demo", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
