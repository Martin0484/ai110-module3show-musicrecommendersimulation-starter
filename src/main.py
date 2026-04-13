"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs1 = {"genre": "pop", "mood": "happy", "energy": 0.8}
    user_prefs2 = {"genre": "lofi", "mood": "chill", "energy": 0.8}
    user_prefs3 = {"energy": 0.93, "tempo_bpm": 132, "valence": 0.77, "danceability": 0.88, "acousticness": 0.05}
    user_prefs4 = {"genre": "lofi", "mood": "chill"}
    user_prefs = {"genre": "rock", "mood": "energetic", "energy": 0.9}

    recommendations = recommend_songs(user_prefs4, songs, k=5)

    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


if __name__ == "__main__":
    main()
