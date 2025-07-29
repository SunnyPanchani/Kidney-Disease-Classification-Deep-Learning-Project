import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        # Get the absolute path to the model
        model_path = os.path.abspath("model/model.tflite")
        print(f"Loading model from: {model_path}")
        
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at {model_path}")
        
        self.interpreter = tf.lite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

    def predict(self):
        # Load and preprocess image
        img = image.load_img(self.filename, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        # Run inference
        self.interpreter.set_tensor(self.input_details[0]['index'], img_array.astype(np.float32))
        self.interpreter.invoke()
        output_data = self.interpreter.get_tensor(self.output_details[0]['index'])

        # Process results
        predicted_class = np.argmax(output_data, axis=1)[0]
        confidence = float(output_data[0][predicted_class])
        
        labels = {0: "Normal", 1: "Tumor"}
        return [{
            "prediction": labels[predicted_class],
            "confidence": round(confidence, 4)
        }]