# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.


---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Attempt limit per difficulty (Easy 8, Normal 6, Hard 4) | "The number of guesses given for each difficulty level is wrong. For easy it should be 8, for normal it should be 6, and for hard it should be 4. Make changes to the code to reflect this and create a test to verify it." | `test_attempt_limits` — asserts `get_attempt_limit()` returns 8 / 6 / 4. The AI first moved the limits out of `app.py` into `logic_utils.py` so they could be tested. | Yes | The limits were hard-coded in the Streamlit script (6 / 8 / 5), where a unit test couldn't reach them. Moving them into a function made the bug fixable and testable in one place. |
| Very large numbers | "Add to the tests, separate cases for very large numbers, negative numbers, and numbers with a decimal point." | `test_very_large_numbers` — `"99999999999999999999"` parses exactly and compares as "Too High"; `"1.5e400"` returns "That is not a number." | No at first — `"1.5e400"` crashed with `OverflowError`. Passed after adding `OverflowError` to the `except` in `parse_guess`. | The test exposed a real crash: a decimal too big for a float becomes infinity, and `int(inf)` raises an error the code didn't catch. |
| Negative numbers | (same prompt as above) | `test_negative_numbers` — `"-5"` and `"-0"` parse; a negative guess is "Too Low"; a lone `"-"` is rejected. | Yes | Showed that negatives were accepted even though no difficulty's range includes them, which led to the range check below. |
| Numbers with a decimal point | (same prompt as above) | `test_decimal_numbers` — `"3.0"`→3, `"1.5"`→1, `"-7.9"`→-7, `".5"`→0, `"5."`→5; `"1.2.3"` is rejected. | Yes | Confirms decimals are truncated toward zero rather than rounded, and that malformed decimals don't sneak through. |
| Guesses outside the difficulty range | "add range check to stop very large numbers, and instead show an error message." | `test_range_check` — 1 and 20 are accepted on Easy; 0, 21 and -5 are rejected with "Guess must be between 1 and 20."; `"20.9"` truncates to 20 and is accepted. Plus `test_out_of_range_guess_shows_error`, which runs the app and checks the error appears. | Yes | Tests both edges of the range plus just outside them, and a UI-level test confirms the player actually sees the message. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
