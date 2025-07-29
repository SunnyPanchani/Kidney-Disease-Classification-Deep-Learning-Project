from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
import os
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add src directory to Python path
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'src'))
sys.path.insert(0, src_path)
logger.info(f"Added to PATH: {src_path}")

try:
    from cnnClassifier.utils.common import decodeImage
    from cnnClassifier.pipeline.prediction import PredictionPipeline
    logger.info("Successfully imported prediction modules")
except ImportError as e:
    logger.error(f"Import error: {e}")
    raise

# Set locale for compatibility (optional)
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Verify model exists before starting
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model", "model.tflite")
MODEL_PATH = os.path.abspath(MODEL_PATH)

logger.info(f"Current working directory: {os.getcwd()}")
logger.info(f"Model path: {MODEL_PATH}")

if not os.path.exists(MODEL_PATH):
    logger.error(f"ERROR: Model file not found at {MODEL_PATH}")
    model_dir = os.path.dirname(MODEL_PATH)
    if os.path.exists(model_dir):
        logger.error(f"Files in model directory: {os.listdir(model_dir)}")
    else:
        logger.error(f"Model directory does not exist: {model_dir}")
else:
    logger.info(f"Model verified at: {MODEL_PATH}")

# Main class for prediction
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        try:
            logger.info("Initializing PredictionPipeline...")
            self.classifier = PredictionPipeline(self.filename)
            logger.info("PredictionPipeline initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing PredictionPipeline: {e}")
            raise

# Instantiate once globally
try:
    clApp = ClientApp()
    logger.info("ClientApp instantiated successfully")
except Exception as e:
    logger.error(f"Failed to create ClientApp: {e}")

# Home route
@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

# Training route
@app.route("/train", methods=['GET', 'POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training completed successfully!"

# Prediction route
@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        logger.info("Received image data.")
        decodeImage(image, clApp.filename)
        logger.info("Image decoded and saved.")
        
        # Verify the image exists
        image_path = os.path.abspath(clApp.filename)
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Decoded image not found at {image_path}")
        logger.info(f"Image verified at: {image_path}")
            
        result = clApp.classifier.predict()
        logger.info("Prediction complete.")
        return jsonify(result)
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return jsonify({"error": str(e)}), 500

# Run app
if __name__ == "__main__":
    logger.info("Starting Flask application...")
    app.run(host='0.0.0.0', port=8080, debug=True)









# from flask import Flask, request, jsonify, render_template
# from flask_cors import CORS, cross_origin
# import os
# import sys
# import logging
# from datetime import datetime
# import base64

# # Logging setup
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Add src to path
# src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'src'))
# sys.path.insert(0, src_path)

# try:
#     from cnnClassifier.utils.common import decodeImage
#     from cnnClassifier.pipeline.prediction import PredictionPipeline
# except ImportError as e:
#     logger.error(f"Import error: {e}")
#     raise

# # Flask setup
# app = Flask(__name__)
# CORS(app)

# # Model file check
# MODEL_PATH = os.path.abspath("model/model.h5")
# if not os.path.exists(MODEL_PATH):
#     logger.error(f"Model file not found at {MODEL_PATH}")
# else:
#     logger.info(f"Model verified at {MODEL_PATH}")

# # Main prediction class
# class ClientApp:
#     def __init__(self):
#         self.filename = None  # dynamic per image
#         self.classifier = None  # init later for each image

# clApp = ClientApp()

# # Home route
# @app.route("/", methods=['GET'])
# @cross_origin()
# def home():
#     return render_template('index.html')

# # Training route
# @app.route("/train", methods=['GET', 'POST'])
# @cross_origin()
# def trainRoute():
#     os.system("python main.py")
#     return "Training completed successfully!"

# # Prediction route for multiple images
# @app.route("/predict", methods=['POST'])
# @cross_origin()
# def predictRoute():
#     try:
#         images = request.json['images']  # expects list of base64 images
#         logger.info(f"Received {len(images)} images for prediction.")

#         results = []

#         for idx, img_str in enumerate(images):
#             # Prepare unique filename
#             timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
#             filename = f"inputImage_{idx}_{timestamp}.jpg"
#             clApp.filename = filename

#             # Decode image
#             decodeImage(img_str, filename)
#             logger.info(f"Saved image {filename}")

#             # Predict
#             clApp.classifier = PredictionPipeline(filename)
#             result = clApp.classifier.predict()
#             results.append({
#                 "image": filename,
#                 "prediction": result[0]["prediction"],
#                 "confidence": result[0]["confidence"]
#             })

#         return jsonify({"results": results})

#     except Exception as e:
#         logger.error(f"Prediction error: {e}")
#         return jsonify({"error": str(e)}), 500

# # Run app
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8080, debug=True)
