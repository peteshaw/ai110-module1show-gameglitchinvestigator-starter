"""Tests that drive the Streamlit app and check what the player sees."""

from pathlib import Path

from streamlit.testing.v1 import AppTest

APP_PATH = str(Path(__file__).resolve().parent.parent / "app.py")


def submit_guess(guess, secret=25):
    """Run the app, submit one guess, and return the warning messages shown.

    The secret is set directly so the expected hint is known.
    """
    at = AppTest.from_file(APP_PATH)
    at.run()
    at.session_state.secret = secret
    at.text_input[0].input(str(guess))
    at.button[0].click()
    at.run()
    return [w.value for w in at.warning]


def test_too_high_guess_shows_go_lower():
    """A guess above the secret shows the "Go LOWER!" hint."""
    # Guess above the secret should tell the player to go lower
    assert submit_guess(40) == ["Go LOWER!"]


def test_too_low_guess_shows_go_higher():
    """A guess below the secret shows the "Go HIGHER!" hint."""
    # Guess below the secret should tell the player to go higher
    assert submit_guess(10) == ["Go HIGHER!"]


def test_out_of_range_guess_shows_error():
    """A guess outside the Normal range shows a range error."""
    at = AppTest.from_file(APP_PATH)
    at.run()
    at.text_input[0].input("99999999999999999999")
    at.button[0].click()
    at.run()
    assert [e.value for e in at.error] == ["Guess must be between 1 and 50."]
