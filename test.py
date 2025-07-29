# import getpass
# print(getpass.getuser())
# import mlflow
# print(mlflow.get_tracking_uri())

# import os
# import mlflow

# # Set tracking URI and credentials
# os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/SunnyPanchani/Kidney-Disease-Classification-Deep-Learning-Project.mlflow"
# os.environ["MLFLOW_TRACKING_USERNAME"] = "SunnyPanchani"
# os.environ["MLFLOW_TRACKING_PASSWORD"] = "51e674af3ed024048b584380ab52974ad8982d12"

# print("✅ Tracking URI set to:", mlflow.get_tracking_uri())






# import sys, os
# sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
# from cnnClassifier.pipeline.prediction import PredictionPipeline

# from tensorflow.keras.preprocessing.image import ImageDataGenerator

# datagen = ImageDataGenerator(rescale=1./255)
# gen = datagen.flow_from_directory("artifacts/data_ingestion/kidney-ct-scan-image", target_size=(224,224))

# print(gen.class_indices)

# print("Image shape:", img_array.shape)
# print("Model output:", output_data)


# print("Loading model: model/model.tflite")
import os
from src.cnnClassifier.pipeline.prediction import PredictionPipeline

print("Testing prediction pipeline...")
print("Current directory:", os.getcwd())

# Test with a sample image
predictor = PredictionPipeline("123.jpg")
result = predictor.predict()
print("Prediction result:", result)






# import os

# for root, dirs, files in os.walk("mlruns"):
#     for file in files:
#         if file.endswith(".yaml") or file.endswith(".json"):
#             path = os.path.join(root, file)
#             with open(path, "r") as f:
#                 if "jay" in f.read():
#                     print("Found in:", path)
