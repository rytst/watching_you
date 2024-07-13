from ultralytics import YOLO


# Load a model
model = YOLO("yolov8n.pt")  # pretrained YOLOv8n model



def count_person(image):

    
    # prediction
    result = model(image)
    
    
    boxes = result[0].boxes  # Boxes object for bounding box outputs
    
    labels = boxes.cls # Return the class values of the boxes
    
    n_person = (labels==0).sum().item()

    # result.show()  # display to screen
    # result[0].save(filename="result.jpg")  # save to disk
    
    return n_person


# image = 'test01.jpg'
# num_of_person = count_person(image)
# print('num_of_person:', num_of_person)
