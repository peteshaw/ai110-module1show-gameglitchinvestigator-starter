# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- While the game looked fine, its performance was filled with many errors and bugs. 
- More detailed information on the bugs and screenshots are included in the assignment_log.md file.   I did not want to change the format of this document, so I just collected my notes and development steps there, and copied over as necessary. 
**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| # | Input | Expected Behavior | Actual Behavior | Console Output / Error |
|---|-------|-------------------|-----------------|------------------------|
| 1 | Entered `25` as a guess (debug info showed `22`) | App displays **"Go Lower"** | App displayed **"Go Higher"** | Screenshot: `screenshots/Bug1-Screenshot.png` |
| 2 | Selected **Normal** difficulty | Range should be **1–50** | Range was **1–100**; also, selecting **Hard** difficulty resulted in a range of **1–50** (inverted/wrong ranges), this was caused by the  | Screenshot: `screenshots/Bug2-Screenshot.png` |
| 3 | Selected **Normal** difficulty | Consistent number of guesses across UI; guesses should decrease as difficulty increases (Easy = 8, Normal = 6, Hard = 4) | Settings showed **8** guesses; blue bar showed **7** (mismatch). Guess count logic also incorrect across difficulties | Screenshot: `screenshots/Bug3-Screenshot.png` |
| 4 | Clicked **New Game** button | "Game Over" message disappears and a fresh game starts (all game elements re-initialized) | Game interface did not reset and a new game could not be played. Occurred **intermittently** |
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - For this assigment I used ChatGPT within Visual Studio Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - When I asked Claude to explain the logic of the Parse_Guess function to me, Claud successfully noted the flwaed logic of the function.  The error was that the guess was being passed as a string and then when asked, provided a fix for this issue, which was to provide an integer value on the gui side.
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
- Claude kept wanting the response for a "too high" result to be "Go Higher" in the game UI, specificallly in the Check Guess .  I had to specify that he change the response to "Too High" to "Go Lower", and to create a test to verify this. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - A combination of manual testing and code inspection.   For a larger project I imagine I would need larger and more thorough testing. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
 -   Claude ended up creating a separate test for the game hints, hoswing me that Streamlit has a built in Apptest feature for testing UI elements separate from python logic. 

- Did AI help you design or understand any tests? How?
  - In my coding I have not used test driven development or really any testing with any depth.  Now I have a better understanding of the how and why of test driven development.  Looking at the tests forced me to realize that the error in guessing can be caused by treating a number as a string, or an integer or as a float, which are both cases that need to be avoided. 


---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
 - Interesting model, it basically runs the web page as  a top to bottom app.   Most of my knowledge of javascript and web page programming tends to descrive web programming in terms of asynchronous calls, so this was much simpler gerally. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - Test driven development.  AI  makes creating and using tests *MUCH* simpler and I could very quickly see the value in this. 
- What is one thing you would do differently next time you work with AI on a coding task?
  - Tracking all my changes from the start.  I didn't keep track of my conversations with Claude initially, and this made it hard for me to go back and write up the changes that I made.  
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - In the past I have used AI to mostly create a procedure or function to solve a specific problem.  Mostly using powershell scripts to automate tasks or fix problems with Microsoft 365.  This was an introduction to me of using AI to understand an existing body of code. 
