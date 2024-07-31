import os
import pandas as pd
import joblib
from prediction_model.config import config

#Load the dataset
def load_dataset(file_name):
    filepath = os.path.join(config.DATAPATH, file_name)
    data = pd.read_csv(filepath)
    return data

# serialization
def save_pipeline(pipeline_to_save):
    save_path = os.path.join(config.SAVE_MODEL_PATH, config.MODEL_NAME)
    joblib.dump(pipeline_to_save, save_path)
    print(f"model saved at: {config.MODEL_NAME}")



# Deserialization
def load_pipeline(pipeline_to_save):
    save_path = os.path.join(config.SAVE_MODEL_PATH, config.MODEL_NAME)
    model_loaded = joblib.load(save_path)
    print(f"model has been loaded from: {config.MODEL_NAME}")
    return model_loaded