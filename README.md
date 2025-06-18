# CarlsenMeter

This project is a machine learning application that analyzes chess games to determine how closely a player's style matches that of Magnus Carlsen.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/kauanhindlmayer/carlsenmeter.git
cd carlsenmeter
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

1. Place your `.pgn` files in the `data/` folder.
2. Run the application:

```bash
python -m src.carlsenmeter
```

The system will process the games and output your score, indicating how stylistically close you are to Magnus Carlsen.
