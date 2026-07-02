"""
ONNX Runtime inference engine.
"""

import numpy as np
import onnxruntime as ort


class ONNXClassifier:

    def __init__(self, model_path, class_names):

        self.class_names = class_names

        self.session = ort.InferenceSession(
            model_path,
            providers=ort.get_available_providers()
        )

        self.input_name = self.session.get_inputs()[0].name
        self.output_name = self.session.get_outputs()[0].name

    def predict(self, input_tensor):

        logits = self.session.run(
            [self.output_name],
            {self.input_name: input_tensor}
        )[0]

        logits = logits.squeeze()

        # Softmax
        exp = np.exp(logits - np.max(logits))
        probabilities = exp / exp.sum()

        class_index = np.argmax(probabilities)

        confidence = probabilities[class_index]

        return (
            self.class_names[class_index],
            float(confidence)
        )