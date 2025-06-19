import numpy as np
from src.feature_extraction import extract_features

def prepare_input_features(games, eco_encoder):
  feature_list = []
  eco_codes = []

  for game in games:
    features = extract_features(game)
    eco_codes.append(features["eco"])
    feature_list.append(features)

  eco_numeric = eco_encoder.transform(eco_codes)

  X = np.array([
    [
      row["total_moves"],
      eco_numeric[idx],
      row["white_moves"],
      row["black_moves"]
    ]
    for idx, row in enumerate(feature_list)
  ])

  return X