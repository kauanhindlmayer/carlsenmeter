import chess.pgn

def load_games(pgn_file_path, max_games=1000):
  games = []
  with open(pgn_file_path, encoding='utf-8') as pgn:
    while len(games) < max_games:
      game = chess.pgn.read_game(pgn)
      if game is None:
        break
      games.append(game)
  return games
