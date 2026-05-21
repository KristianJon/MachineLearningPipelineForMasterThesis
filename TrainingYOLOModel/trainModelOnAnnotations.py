from ultralytics import YOLO

def main():
    model = YOLO("yolo12m.pt")
    model.train(
        data="dataset.yaml",
        epochs=300,
        imgsz=640,
        batch=8,
	patience=100,
        device=0, #"cpu" or "0" for gpu
        workers=0,
	single_cls=True
    )

    model.export(format="torchscript")

if __name__ == "__main__":
    main()