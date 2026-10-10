# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [X] Describe the game's purpose.
  - This game is a demo of the streamlit framework, and is a simple number guessing game, where you can choose 1 of 3 levels, and try to guess a secret number within a limited number of guesses. 
- [X] Detail which bugs you found.
  - As I detailed in the reflection.md file, I found at least 4 bugs.  
      1. The hints were in the reverse directions
      2. The numeric guesses were not getting compared correctly with the secret.
      3. The state was not getting properly reset after a finished game.
      4. The count of guesses left was not being correctly incremented. 
- [X] Explain what fixes you applied.
    - Using Claude code, I was able to move the logic of the applicaiton to the logic_utils.py file.  I was also able to create a number of tests for the application to verify that it all was working properly. 
  - 

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Select the difficulty from the dropdown on the left hand side of the application.  There are three levels, easy, medium, and hard.  Easy has a secret value of 1 to 20, medium is 1 to 50, and hard is 1 to 100.  For each level you get a number of guesses.  Easy you get 8 guesses, medium is 6 guessses, and hard is 4 guesses.
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
