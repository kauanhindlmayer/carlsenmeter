from src.data_processing import load_games
from src.feature_extraction import aggregate_features
from src.similarity_calculation import calculate_similarity

def main():
  carlsen_games = load_games("data/carlsen_games.pgn")
  other_games = load_games("data/other_players.pgn")

  carlsen_features = aggregate_features(carlsen_games)
  player_features = aggregate_features(other_games)

  score = calculate_similarity(player_features, carlsen_features)

  print("=== CarlsenMeter Score ===")
  print(f"Similarity Score: {score} / 100")

if __name__ == "__main__":
  main()
