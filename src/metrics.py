"""
metrics.py

Performance metrics for live inference.
"""

import time


class PerformanceMetrics:

    def __init__(self):

        self.previous_time = time.perf_counter()

        self.total_frames = 0

        self.total_latency = 0.0

        self.start_time = time.perf_counter()

    def calculate_fps(self):

        current_time = time.perf_counter()

        fps = 1.0 / (current_time - self.previous_time)

        self.previous_time = current_time

        return fps

    @staticmethod
    def calculate_latency(start_time):

        return (time.perf_counter() - start_time) * 1000

    def update(self, latency):

        self.total_frames += 1

        self.total_latency += latency

    def summary(self):

        elapsed = time.perf_counter() - self.start_time

        avg_fps = self.total_frames / elapsed

        avg_latency = self.total_latency / self.total_frames

        throughput = avg_fps

        return {
            "frames": self.total_frames,
            "elapsed": elapsed,
            "avg_fps": avg_fps,
            "avg_latency": avg_latency,
            "throughput": throughput,
        }