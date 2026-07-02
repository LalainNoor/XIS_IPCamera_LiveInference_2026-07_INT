# Experiment Log

## Date
2026-07-02

## Objective

Develop a live IP camera inference pipeline capable of receiving frames from an IP camera (RTSP/HTTP), performing real-time image classification using ONNX Runtime, and displaying live predictions with performance metrics.

---

## Environment

- Windows
- Python Virtual Environment
- OpenCV
- ONNX Runtime
- NumPy
- IP Webcam (Android)
- Visual Studio Code

---

## Camera Configuration

### Supported Camera Modes

- Video File
- USB Webcam
- IP Camera (RTSP/HTTP)

For live testing, an Android phone running the **IP Webcam** application was used as the IP camera source over the local Wi-Fi network.

The application was configured to receive the live stream through an HTTP/RTSP endpoint using OpenCV's `VideoCapture`.

---

## Camera Module

Implemented a modular camera interface capable of:

- Reading frames from a video file.
- Capturing frames from a USB webcam.
- Connecting to an IP camera stream.
- Automatically attempting reconnection when the stream is interrupted.
- Providing a unified interface for the inference pipeline.

---

## Preprocessing

Each captured frame undergoes the following preprocessing steps:

- Convert BGR to RGB.
- Resize to 224 × 224 pixels.
- Normalize pixel values.
- Convert image to CHW format.
- Create an ONNX Runtime input tensor.

---

## Inference

- Loaded the ConvNeXt V2 ONNX model.
- Performed real-time image classification.
- Predicted the scene class for every frame.
- Computed prediction confidence.

---

## Performance Monitoring

The application continuously measured:

- Frames Per Second (FPS)
- Inference Latency
- Throughput
- Total Processed Frames
- Processing Time

Performance statistics were automatically saved to:

```text
results/performance/performance.txt
```

---

## Results

Successfully achieved:

- Live IP camera streaming.
- Real-time ONNX Runtime inference.
- Live prediction overlay.
- FPS and latency monitoring.
- Throughput calculation.
- Automatic stream reconnection attempt after connection loss.
- Performance report generation.

---

## Observations

- The HTTP stream provided stable live inference using OpenCV.
- RTSP streaming worked but occasionally experienced H.264 decoding issues depending on the stream configuration.
- The modular camera design allows switching between video files, USB webcams, and IP cameras without modifying the inference pipeline.

---

## Conclusion

The project successfully demonstrated a complete live IP camera inference pipeline capable of processing network camera streams using ONNX Runtime. The implementation supports multiple camera sources while maintaining a unified GPU inference workflow and real-time performance monitoring.