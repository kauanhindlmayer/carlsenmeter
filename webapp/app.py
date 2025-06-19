from flask import Flask, render_template, request, redirect, url_for
import numpy as np
from joblib import load
from src.data_preprocessing import load_games
from src.feature_extraction import extract_features, encode_eco
from src.feature_preparation import prepare_input_features

app = Flask(__name__)

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

@app.route("/", methods=["GET", "POST"])
def index():
  score = None
  message = None

  if request.method == "POST":
    file = request.files.get("pgn_file")
    if file:
      filepath = "./temp_uploaded.pgn"
      file.save(filepath)
      score = prepare_features_for_prediction(filepath)

      if score >= 80:
        message = "You're a Magnus twin!"
      elif score >= 50:
        message = "Solid Carlsen vibes."
      elif score >= 30:
        message = "Some Magnus in you."
      else:
        message = "Plenty of room to grow!"

  return render_template("index.html", score=score, message=message)

if __name__ == "__main__":
  app.run(debug=True)
