"""
Utilities for drawing inference results.
"""

import cv2


def draw_overlay(
    frame,
    prediction,
    confidence,
    fps=None,
    latency=None,
    throughput=None,
):

    cv2.putText(
        frame,
        f"Prediction : {prediction}",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2,
    )

    cv2.putText(
        frame,
        f"Confidence : {confidence:.2%}",
        (20, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2,
    )

    if throughput is not None:

        cv2.putText(
            frame,
            f"Throughput : {throughput:.2f} FPS",
            (20, 175),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 0),
            2,
        )

    if fps is not None:

        cv2.putText(
            frame,
            f"FPS : {fps:.2f}",
            (20, 105),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 0),
            2,
        )

    if latency is not None:

        cv2.putText(
            frame,
            f"Latency : {latency:.2f} ms",
            (20, 140),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 0),
            2,
        )

    return frame