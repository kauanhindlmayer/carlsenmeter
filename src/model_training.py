import numpy as np
from src.data_preprocessing import load_games
from src.feature_extraction import extract_features, encode_eco
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from joblib import dump
import os

def prepare_dataset(carlsen_games, other_games):
  X = []
  y = []

  all_eco_codes = []

  for game in carlsen_games:
    features = extract_features(game)
    X.append(features)
    y.append(1)
    all_eco_codes.append(features["eco"])

  for game in other_games:
    features = extract_features(game)
    X.append(features)
    y.append(0)
    all_eco_codes.append(features["eco"])

  eco_numeric, le = encode_eco(all_eco_codes)

  for idx, row in enumerate(X):
    row["eco"] = eco_numeric[idx]

  feature_matrix = np.array([[row["total_moves"], row["eco"], row["white_moves"], row["black_moves"]] for row in X])

  return feature_matrix, np.array(y), le

def train_model(X, y, le):
  X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
  model = RandomForestClassifier(n_estimators=100, random_state=42)
  model.fit(X_train, y_train)

  os.makedirs("models", exist_ok=True)
  dump(model, "models/carlsenmeter_model.joblib")
  dump(le, "models/eco_encoder.joblib")

  return model
