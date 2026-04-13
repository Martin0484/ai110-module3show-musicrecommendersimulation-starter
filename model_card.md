# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

BeatMatcher 1.0

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration 

It is designed to recommend songs based on features like mood and genre.
It is for real users who are looking for new songs to listen to.
The recommender assumes that the user will often listen to only a specific
type of music.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

Genre and mood contribute the most points for scoring. Many user preferences like
energy, tempo_bpm, and valence are considered. The model turns them into a score
by getting floats from them and adding them up.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

18 songs are in the catalog. Lofi and chill are represented frequently.
I added songs 11 through 18. Language is a part of the musical taste
missing in the dataset.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

It gives reasonable results for users with a complete set of information.
I think patterns in genre are captured correctly. Midnight Coding being
ranked first matched my intuition.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The system is case-sensitive for genre. So "rock" and "Rock" are not seen as
matches. This can lead to songs not getting recommended even though they should be.
---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

All user profiles were tested and I was surprised that Midnight
Coding got a very high score.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

I would eliminate case sensitivity so capitilization of letters or lack there of
would not lead to mismatches.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

I learned that recommender systems rely on weights given to attributes
to make decisions. I discovered that a song's match can be reduced to
a single number.
