# IP Camera Live Inference

## Overview

This project implements a live IP camera inference pipeline using OpenCV and ONNX Runtime. The application captures frames from an IP camera stream (RTSP/HTTP), performs real-time image classification using a ConvNeXt V2 ONNX model, and displays live predictions along with performance metrics.

The pipeline supports multiple camera sources, including video files, USB webcams, and IP cameras, with automatic reconnection handling for interrupted network streams.

---

## Objectives

- Connect to an IP camera using RTSP or HTTP streaming.
- Capture live frames using OpenCV.
- Run GPU-accelerated ONNX Runtime inference on each frame.
- Display live predictions with confidence scores.
- Measure FPS, inference latency, and throughput.
- Handle network interruptions with automatic stream reconnection.

---

## Features

- IP Camera (RTSP/HTTP) support
- USB Webcam support
- Video file support for testing
- Modular camera interface
- Automatic reconnection for interrupted streams
- ConvNeXt V2 ONNX inference
- Real-time prediction overlay
- FPS monitoring
- Inference latency measurement
- Throughput calculation
- Automatic performance report generation

---

## Project Structure

```text
XIS_IPCamera_LiveInference_2026-07_INT/

├── input/
│   └── sample_video.mp4
│
├── models/
│   ├── convnextv2.onnx
│   └── convnextv2.onnx.data
│
├── notebooks/
│   └── 1_IPCamera_LiveInference.ipynb
│
├── results/
│   ├── performance/
│   │   └── performance.txt
│   └── screenshots/
│       └── ip_camera_live_inference.png
│
├── src/
│   ├── camera.py
│   ├── config.py
│   ├── display.py
│   ├── inference.py
│   ├── main.py
│   ├── metrics.py
│   └── preprocess.py
│
├── README.md
├── experiment_log.md
├── requirements.txt
└── .gitignore
```

---

## Model

**Model:** ConvNeXt V2 (ONNX)

### Classes

- buildings
- forest
- glacier
- mountain
- sea
- street

---

## Camera Modes

The application supports three input sources:

### Video File

Used for testing and debugging.

```python
CAMERA_MODE = "video"
```

---

### USB Webcam

Uses a connected webcam.

```python
CAMERA_MODE = "webcam"
```

---

### IP Camera

Supports RTSP or HTTP streams.

```python
CAMERA_MODE = "rtsp"
```

Example:

```python
RTSP_URL = "http://<ip-address>:8080/video"
```

or

```python
RTSP_URL = "rtsp://<ip-address>:8080/h264.sdp"
```

---

## Performance Metrics

The application measures:

- Average FPS
- Inference Latency
- Throughput
- Total Processed Frames
- Processing Time

Performance reports are automatically saved in:

```text
results/performance/performance.txt
```

---

## Results

The project successfully demonstrates:

- Live IP camera streaming
- Real-time ONNX inference
- Live prediction overlay
- Automatic stream reconnection
- Performance benchmarking

---

## Screenshots

Screenshots of live inference are stored in:

```text
results/screenshots/
```

---

## Requirements

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Run

Execute:

```bash
python src/main.py
```

---

## Future Improvements

- Improve RTSP reconnection robustness.
- Add configurable stream buffering.
- Support multiple simultaneous IP cameras.
- Add TensorRT acceleration.
- Export benchmark results to CSV.