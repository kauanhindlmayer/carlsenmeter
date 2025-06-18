def extract_features(game):
  moves = list(game.mainline_moves())
  total_moves = len(moves)
  opening = game.headers.get("Opening", "Unknown")
  return {
    "total_moves": total_moves,
    "opening": opening,
  }

def aggregate_features(games):
  total_moves_list = [extract_features(g)["total_moves"] for g in games]
  avg_total_moves = sum(total_moves_list) / len(total_moves_list) if total_moves_list else 0
  return {
    "avg_total_moves": avg_total_moves,
    "total_games": len(games),
  }
