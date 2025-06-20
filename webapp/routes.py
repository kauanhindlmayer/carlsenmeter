from flask import Blueprint, render_template, request
from .services import prepare_features_for_prediction

bp = Blueprint('main', __name__)

SCORE_MESSAGES = [
  (80, "You're a Magnus twin!"),
  (50, "Solid Carlsen vibes."),
  (30, "Some Magnus in you."),
  (0,  "Plenty of room to grow!"),
]

def get_message(score):
  return next(msg for threshold, msg in SCORE_MESSAGES if score >= threshold)

@bp.route("/", methods=["GET", "POST"])
def index():
  score = None
  message = None

  if request.method == "POST":
    file = request.files.get("pgn_file")
    if file:
      filepath = "./temp_uploaded.pgn"
      file.save(filepath)
      score = prepare_features_for_prediction(filepath)
      message = get_message(score)

  return render_template("index.html", score=score, message=message)