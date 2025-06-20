import numpy as np
from joblib import load
from src.data_preprocessing import load_games
from src.feature_preparation import prepare_input_features

model = load("models/carlsenmeter_model.joblib")
eco_encoder = load("models/eco_encoder.joblib")

def prepare_features_for_prediction(pgn_file):
  user_games = load_games(pgn_file)
  if not user_games:
    return None

  X = prepare_input_features(user_games, eco_encoder)
  probs = model.predict_proba(X)[:, 1]
  avg_score = np.mean(probs) * 100
  return round(avg_score, 2)