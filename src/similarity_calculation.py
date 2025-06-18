def calculate_similarity(player_features, carlsen_features):
  if carlsen_features["avg_total_moves"] == 0:
    return 0
  diff = abs(player_features["avg_total_moves"] - carlsen_features["avg_total_moves"])
  similarity = max(0, 100 - diff)
  return round(similarity, 2)
