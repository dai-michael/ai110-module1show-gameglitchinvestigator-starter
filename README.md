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

- [x] Game purpose: A number guessing game where the player tries to guess a secret number within a limited number of attempts. After each guess the game gives a hint (Too High / Too Low) and updates the score. The player wins by guessing the correct number before running out of attempts.

- [x] Bugs found:
  1. Hints displayed backward — check_guess returned "Go HIGHER" when the guess was too high and "Go LOWER" when it was too low.
  2. Hints never rendered — st.warning(message) was called inside the submit block, but st.rerun() immediately followed, wiping the message before Streamlit could paint it to the screen.
  3. Score inconsistency — Too High and Too Low outcomes deducted different point amounts, making scoring unpredictable.
  4. Off-by-one on attempts — attempts was initialized to 1 instead of 0, causing the first guess to be counted as the second attempt and reducing win points unfairly.
  5. Secret number type inconsistency — on even-numbered attempts the secret was cast to a string, breaking numeric comparison and causing incorrect hint direction.
  6. New game did not fully reset — starting a new game left the old status, score, and hint message in session state, causing the game over or win screen to immediately reappear.

- [x] Fixes applied:
  1. Swapped the return values in check_guess so Too High maps to Go LOWER and Too Low maps to Go HIGHER.
  2. Stored the hint in session state before the rerun call, then displayed it after the submit block so it survives the rerun cycle.
  3. Made both Too High and Too Low outcomes consistently deduct 5 points in update_score.
  4. Changed the initial value of attempts from 1 to 0.
  5. Removed the even/odd attempt type conversion so the secret remains an integer throughout.
  6. Added resets for status, score, and hint_message inside the new game block.
  7. Refactored all pure logic functions into logic_utils.py and imported them into app.py.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User inputs a guess of 70 -> Game returns "Too High"
2. User inputs a guess of 60 -> Game returns "Too Low"
3. Score updates after each unsuccessful guess
4. User ineputs a guess of 65 -> Correct guess, and game ends
5. Final score displayed and user has the option to start a new game

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
tests/test_game_logic.py ...................................                   [100%]

================================= 35 passed in 0.02s =================================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
