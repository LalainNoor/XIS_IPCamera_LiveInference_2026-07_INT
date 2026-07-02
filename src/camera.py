"""
Universal camera module for Video, USB Webcam, and IP Camera (RTSP).
"""

import cv2
import time

from config import (
    CAMERA_MODE,
    VIDEO_PATH,
    WEBCAM_ID,
    RTSP_URL,
    FRAME_WIDTH,
    FRAME_HEIGHT,
)


class Camera:

    def __init__(self):

        self.cap = None
        self.source = None

        self.connect()

    def connect(self):

        while True:

            if self.cap is not None:
                self.cap.release()

            if CAMERA_MODE == "video":
                self.source = VIDEO_PATH

            elif CAMERA_MODE == "webcam":
                self.source = WEBCAM_ID

            elif CAMERA_MODE == "rtsp":
                self.source = RTSP_URL

            else:
                raise ValueError(f"Unsupported CAMERA_MODE: {CAMERA_MODE}")

        print(f"Connecting to: {self.source}")

        self.cap = cv2.VideoCapture(self.source)

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

        if CAMERA_MODE == "rtsp":
            self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

        if self.cap.isOpened():
            print("Connected successfully.")
            return

        print("Connection failed. Retrying in 2 seconds...")
        time.sleep(2)

    def read(self):

        ret, frame = self.cap.read()

        if ret:
            return ret, frame

        # Reconnect only for RTSP streams
        if CAMERA_MODE == "rtsp":

            print("Connection lost. Reconnecting...")

            self.cap.release()

            time.sleep(2)

            self.connect()

            ret, frame = self.cap.read()

            return ret, frame

        return ret, frame

    def get_width(self):
        return int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    def get_height(self):
        return int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def get_fps(self):
        return self.cap.get(cv2.CAP_PROP_FPS)

    def get_frame_count(self):
        return int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

    def release(self):

        if self.cap is not None:
            self.cap.release()