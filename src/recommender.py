from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file and converts numerical values to floats.
    Required by src/main.py
    """
    print(f"Loading songs from {csv_path}...")
    songs = []
    
    # Columns that should be converted to float
    float_columns = {'energy', 'tempo_bpm', 'valence', 'danceability', 'acousticness'}
    
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert numeric columns to float
            for col in float_columns:
                if col in row:
                    row[col] = float(row[col])
            
            # Convert id to int
            if 'id' in row:
                row['id'] = int(row['id'])
            
            songs.append(row)
    
    return songs

    """Return a (score, reasons) tuple rating how well a song matches user preferences."""
def score_song(song: Dict, user_prefs: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Returns a tuple of (score, reasons):
      - score: float in [0.0, 1.0] — higher means better match
      - reasons: list of strings explaining each contribution
    """
    WEIGHTS = {
        'genre':        0.15,
        'mood':         0.25,
        'energy':       0.30,
        'tempo_bpm':    0.10,
        'valence':      0.10,
        'danceability': 0.05,
        'acousticness': 0.05,
    }

    reasons = []

    def numeric_score(song_val: float, pref_val: float, value_range: float) -> float:
        return max(0.0, 1.0 - abs(song_val - pref_val) / value_range)

    # Categorical scores
    genre_score = 1.0 if song.get('genre') == user_prefs.get('genre') else 0.0
    mood_score  = 1.0 if song.get('mood')  == user_prefs.get('mood')  else 0.0

    genre_contrib = WEIGHTS['genre'] * genre_score
    mood_contrib  = WEIGHTS['mood']  * mood_score

    if genre_score == 1.0:
        reasons.append(f"genre match (+{genre_contrib:.2f})")
    if mood_score == 1.0:
        reasons.append(f"mood match (+{mood_contrib:.2f})")

    # Numeric scores
    numeric_attrs = [
        ('energy',       user_prefs.get('energy', 0.5),       1.0),
        ('tempo_bpm',    user_prefs.get('tempo_bpm', 120),     140.0),
        ('valence',      user_prefs.get('valence', 0.5),       1.0),
        ('danceability', user_prefs.get('danceability', 0.5),  1.0),
        ('acousticness', user_prefs.get('acousticness', 0.5),  1.0),
    ]

    total = genre_contrib + mood_contrib
    for attr, pref_val, value_range in numeric_attrs:
        attr_score  = numeric_score(song[attr], pref_val, value_range)
        contrib     = WEIGHTS[attr] * attr_score
        total      += contrib
        reasons.append(f"{attr} similarity (+{contrib:.2f})")

    return round(total, 4), reasons

    """Score all songs against user preferences and return the top k sorted by score."""
def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    Expected return format: (song_dict, score, explanation)
    """
    def to_result(song):
        score, reasons = score_song(song, user_prefs)
        return (song, score, ", ".join(reasons))

    return sorted(
        [to_result(song) for song in songs],
        key=lambda x: x[1],
        reverse=True
    )[:k]
