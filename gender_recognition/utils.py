import librosa
import numpy as np
import tensorflow as tf
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "gender_model.h5")



def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=22050)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)  # Extract 20 MFCCs
    return np.mean(mfcc, axis=1).reshape(1, -1)  # Ensure shape (1, 20)


def predict_gender(file_path):
    model = tf.keras.models.load_model(MODEL_PATH)
    features = extract_features(file_path)
    prediction = model.predict(features)
    print(prediction[0][0])
    return "Male" if prediction[0][0] > 0.5 else "Female"
