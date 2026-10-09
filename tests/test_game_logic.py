from logic_utils import check_guess, get_range_for_difficulty, parse_guess

def test_difficulty_ranges():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 50)
    assert get_range_for_difficulty("Hard") == (1, 100)

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_numeric_strings_are_compared_by_integer_value():
    assert check_guess("10", "2") == "Too High"

def test_parse_guess():
    # Valid integer input
    assert parse_guess("42") == (True, 42, None)
    # Decimal input is truncated to an int
    assert parse_guess("7.9") == (True, 7, None)
    # Empty or missing input
    assert parse_guess("") == (False, None, "Enter a guess.")
    assert parse_guess(None) == (False, None, "Enter a guess.")
    # Non-numeric input
    assert parse_guess("abc") == (False, None, "That is not a number.")
