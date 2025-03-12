from ultralytics import YOLO

# YOLOv8 modelini yükle
model = YOLO('yolov8n.pt')

# Bir görüntü üzerinde tahmin yap
results = model('SaçmaGöz.MOV')

# Sonuçları görselleştir
for result in results:
    result.show()
