from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt")  # pretrained YOLOv8n model

# prediction
result = model("test02.jpg")


boxes = result[0].boxes  # Boxes object for bounding box outputs

labels = boxes.cls # Return the class values of the boxes
# print(labels)


try:
    if labels[0] < 1:
        print("Person Detected!!") # the label of person is 0
except Exception:
    pass


# result.show()  # display to screen
result[0].save(filename="result.jpg")  # save to disk
