from lobe import ImageModel
import cv2  # OpenCV controls your camera

# 1. Load your trained AI brain 
model = ImageModel.load('./Plastic_Sorter_Model')

# 2. Turn on your laptop camera
camera = cv2.VideoCapture(0)

print("--- AI Sorter System Online ---")

while True:
    # 3. Capture a live snapshot picture from the webcam stream
    ret, frame = camera.read()
    
    # 4. Pass the picture to Lobe to identify and classify it
    result = model.predict(frame)
    prediction = result.prediction  # This gets the winning label text
    
    # 5. Display a live window pop-up on your laptop showing the camera
    cv2.imshow('Live Sorting Feed', frame)
    
    # 6. Sorting logic commands
    if prediction == "Recyclable Plastic":
        print("MATCH: Recyclable Plastic -> Output: Route Left")
    elif prediction == "Non-Recyclable Plastic":
        print("MATCH: Non-Recyclable Plastic -> Output: Route Right")
    elif prediction == "Background":
        print("Status: Waiting for plastic...")

    # Press 'q' on your laptop keyboard to turn the system off safely
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
