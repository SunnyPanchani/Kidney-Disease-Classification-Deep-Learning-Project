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






import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from cnnClassifier.pipeline.prediction import PredictionPipeline










# import os

# for root, dirs, files in os.walk("mlruns"):
#     for file in files:
#         if file.endswith(".yaml") or file.endswith(".json"):
#             path = os.path.join(root, file)
#             with open(path, "r") as f:
#                 if "jay" in f.read():
#                     print("Found in:", path)
