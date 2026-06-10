# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
When I started, it looked like a number guessing game. The first issue I found was that it looked like hints were backward. Additionallly, score did not reset when new game was called. Another issue is that the secret changed between every guess. When the game ended from the player running out of attempts, the player is blocked from starting a new game. The tracker for attempts left also lags behind the actual intended number of attempts left by one. 


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess 60 when secret = 80 | Too low         |    Too High    |      None
| New game called| Score resets   | Score carries over |  None
| Player loses game and clicks new game| New game starts  |    New game does not start   |    None 
| First attempt inputted | Attempts left decreases by one  |  Attempts left does not change   |  None
| Attempt wrong answer when attempts left is displayed as two |  Player gets one more attempt    | Player loses  None

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I used Claude code for this project. One example where Claude was misleading was when I asked it to understand why attempts left always lagged behind by one. Claude assumed that the issue solelly was because attempts initializes at 1 instead of 0. This was part of the issue, but I verified that it did not fully fix the problem because manual testing found that attempts still lagged behind by one.
One example where Claude was correct was when I asked it to fix why 5 is added to current score when attempt number is even, and it correctly identified that this behavior made no sense and fixed it, which I verified through doing the same manual test as when I found the bug. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
I decided whether a bug was really fixed by looking at the original behavior and intended behavior, and making sure the fix actually results the intended behavior. I initially manually test a fix using the original input that I used to discover the bug. If the manual test pasted, using Claude, I would generate tests for each bug, giving it the freedom generate extra test cases for edge cases that I might not have considered. One test I ran using pytest tested if check_guess returned the correct hint, which shows that the original bug is fixed. 


## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns occur when a user interacts with a Streamlit app, which reruns the entire script. Because all the code is being rerun, all stored variables in the code are lost, so session state is necessary to store variables you want to carry over between interactions. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
One habit I will reuse in future labs is I will make sure to understand what the agent is doing at every step, and use that information to be specific in future prompts.
One thing I would do differently next time I work with AI is I will be more diciplined with opening new chat sessions for different fixes and explanations.


COME BACK TO LAST QUESTION LATER
ai generated code not perfect, still need human intervention to check for correct functionality and ensure consistent high level decisions

