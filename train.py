from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO('yolov8n.pt')
    results = model.train(data=f'/Users/HP EliteBook/Downloads/project/FYP-Shoplift-1/data.yaml', epochs=10)