import logging
from src.data_preprocessing import load_games
from src.model_training import prepare_dataset, train_model

def main():
  logging.basicConfig(level=logging.INFO)

  logging.info("Loading games...")
  carlsen_games = load_games("data/carlsen_games.pgn")
  other_games = load_games("data/kasparov_games.pgn")
  logging.info(f"Loaded {len(carlsen_games)} Carlsen games and {len(other_games)} other games.")

  logging.info("Preparing dataset...")
  X, y, eco_encoder = prepare_dataset(carlsen_games, other_games)
  logging.info(f"Dataset prepared with {X.shape[0]} samples and {X.shape[1]} features.")

  logging.info("Starting model training...")
  model = train_model(X, y, eco_encoder)
  logging.info("Model training complete.")

if __name__ == "__main__":
  main()
