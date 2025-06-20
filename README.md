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

1. Run the following script to train the model:

```bash
python -m src.carlsenmeter
```

2. Run the web application to analyze your games:

```bash
python -m webapp.app
```

3. Open your web browser and navigate to `http://localhost:5000` to upload a PGN file containing your chess games and view your analysis results.
