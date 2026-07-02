# =====================================================
# Camera Configuration
# =====================================================

# Available modes:
# "video"  -> Video file
# "webcam" -> USB webcam
# "rtsp"   -> IP Camera (RTSP stream)

CAMERA_MODE = "ip"  # Change this to "webcam" or "rtsp" as needed

# Video File
VIDEO_PATH = "input/sample_video.mp4"

# USB Webcam
WEBCAM_ID = 0

# IP Camera 
RTSP_URL = "http://192.168.18.173:8080/video"


# =====================================================
# Model Configuration
# =====================================================

MODEL_PATH = "models/convnextv2.onnx"

CLASS_NAMES = [
    "buildings",
    "forest",
    "glacier",
    "mountain",
    "sea",
    "street",
]


# =====================================================
# Display Configuration
# =====================================================

WINDOW_NAME = "IP Camera Live Inference"

SHOW_FPS = True


# =====================================================
# Camera Settings
# =====================================================

FRAME_WIDTH = 1024
FRAME_HEIGHT = 576

FRAME_RATE = 30

PIXEL_FORMAT = "BGR"