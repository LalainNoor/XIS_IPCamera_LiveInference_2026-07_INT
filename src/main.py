import cv2
import time

from camera import Camera
from config import *
from preprocess import preprocess
from inference import ONNXClassifier
from display import draw_overlay
from metrics import PerformanceMetrics


def main():

    # Initialize camera
    camera = Camera()

    print("=" * 60)
    print("IP Camera Live Inference")
    print("=" * 60)

    if CAMERA_MODE == "video":
        print("Source Type  : Video File")
        print(f"Video Source : {VIDEO_PATH}")

    elif CAMERA_MODE == "webcam":
        print("Source Type  : USB Webcam")
        print(f"Webcam ID    : {WEBCAM_ID}")

    elif CAMERA_MODE == "rtsp":
        print("Source Type  : RTSP IP Camera")
        print(f"RTSP Stream  : {RTSP_URL}")

    width = camera.get_width()
    height = camera.get_height()
    camera_fps = camera.get_fps()

    print(f"Resolution   : {width} x {height}")

    if camera_fps > 0:
        print(f"FPS          : {camera_fps:.2f}")
    else:
        print("FPS          : Unknown")

    print("=" * 60)

    # Load model
    classifier = ONNXClassifier(
        MODEL_PATH,
        CLASS_NAMES
    )

    metrics = PerformanceMetrics()

    while True:

        ret, frame = camera.read()

        if not ret:

            if CAMERA_MODE == "video":
                print("End of video.")
                break

            # Webcam / RTSP will keep trying
            continue

        start = time.perf_counter()

        input_tensor = preprocess(frame)

        prediction, confidence = classifier.predict(input_tensor)

        latency = metrics.calculate_latency(start)

        metrics.update(latency)

        fps = metrics.calculate_fps()
        throughput = fps

        frame = draw_overlay(
            frame,
            prediction,
            confidence,
            fps,
            latency,
            throughput,
        )

        cv2.imshow(WINDOW_NAME, frame)

        key = cv2.waitKey(1)

        if key == ord("q"):
            break

    # Save performance summary
    summary = metrics.summary()

    with open("results/performance/performance.txt", "w") as f:

        f.write("IP Camera Live Inference\n")
        f.write("=" * 40 + "\n")

        if CAMERA_MODE == "video":
            f.write(f"Video Source : {VIDEO_PATH}\n")

        elif CAMERA_MODE == "webcam":
            f.write(f"Webcam ID : {WEBCAM_ID}\n")

        elif CAMERA_MODE == "rtsp":
            f.write(f"RTSP Stream : {RTSP_URL}\n")

        f.write(f"Resolution       : {width} x {height}\n")
        f.write(f"Total Frames     : {summary['frames']}\n")
        f.write(f"Processing Time  : {summary['elapsed']:.2f} sec\n")
        f.write(f"Average FPS      : {summary['avg_fps']:.2f}\n")
        f.write(f"Average Latency  : {summary['avg_latency']:.2f} ms\n")
        f.write(f"Throughput       : {summary['throughput']:.2f} FPS\n")

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()