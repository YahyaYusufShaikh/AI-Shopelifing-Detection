
from roboflow import Roboflow
rf = Roboflow(api_key="oIQ0i5dmrtFNYJ3qTXy7")
project = rf.workspace("fastnuces-uakqb").project("fyp-shoplift")
version = project.version(1)
dataset = version.download("yolov8")
                