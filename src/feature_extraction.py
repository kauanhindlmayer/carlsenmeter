from sklearn.preprocessing import LabelEncoder

def extract_features(game):
  moves = list(game.mainline_moves())
  total_moves = len(moves)
  eco = game.headers.get("ECO", "Unknown")
  
  white_moves = len([i for i in range(len(moves)) if i % 2 == 0])
  black_moves = len([i for i in range(len(moves)) if i % 2 != 0])

  return {
    "total_moves": total_moves,
    "eco": eco,
    "white_moves": white_moves,
    "black_moves": black_moves,
  }

def encode_eco(eco_list):
  le = LabelEncoder()
  eco_numeric = le.fit_transform(eco_list)
  return eco_numeric, le
