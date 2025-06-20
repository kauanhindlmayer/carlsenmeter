import chess.pgn

def load_games(pgn_file_path, max_games=2500):
  games = []
  with open(pgn_file_path, encoding="latin-1") as pgn:
    while len(games) < max_games:
      game = chess.pgn.read_game(pgn)
      if game is None:
        break
      games.append(game)
  return games
