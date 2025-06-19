from src.data_preprocessing import load_games
from src.model_training import prepare_dataset, train_and_evaluate

def main():
  carlsen_games = load_games("data/carlsen_games.pgn")
  other_games = load_games("data/other_players.pgn")

  X, y, eco_encoder = prepare_dataset(carlsen_games, other_games)
  model = train_and_evaluate(X, y, eco_encoder)

if __name__ == "__main__":
  main()
