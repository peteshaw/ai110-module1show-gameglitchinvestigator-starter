from logic_utils import check_guess, get_attempt_limit, get_range_for_difficulty, parse_guess

def test_difficulty_ranges():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 50)
    assert get_range_for_difficulty("Hard") == (1, 100)

def test_attempt_limits():
    assert get_attempt_limit("Easy") == 8
    assert get_attempt_limit("Normal") == 6
    assert get_attempt_limit("Hard") == 4

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

def test_very_large_numbers():
    # Integers beyond 64 bits are parsed exactly, not rounded
    assert parse_guess("99999999999999999999") == (True, 99999999999999999999, None)
    assert check_guess("99999999999999999999", 50) == "Too High"
    # A decimal too large for a float overflows to infinity and is rejected
    assert parse_guess("1.5e400") == (False, None, "That is not a number.")
    # With a range given, very large numbers are rejected with an error
    assert parse_guess("99999999999999999999", 1, 100) == (False, None, "Guess must be between 1 and 100.")
    assert parse_guess("101", 1, 100) == (False, None, "Guess must be between 1 and 100.")

def test_range_check():
    # Both ends of the range are allowed
    assert parse_guess("1", 1, 20) == (True, 1, None)
    assert parse_guess("20", 1, 20) == (True, 20, None)
    # Just outside either end is rejected
    assert parse_guess("0", 1, 20) == (False, None, "Guess must be between 1 and 20.")
    assert parse_guess("21", 1, 20) == (False, None, "Guess must be between 1 and 20.")
    assert parse_guess("-5", 1, 20) == (False, None, "Guess must be between 1 and 20.")
    # Decimals are truncated before the range check
    assert parse_guess("20.9", 1, 20) == (True, 20, None)

def test_negative_numbers():
    assert parse_guess("-5") == (True, -5, None)
    assert parse_guess("-0") == (True, 0, None)
    assert check_guess(-5, 1) == "Too Low"
    # A lone minus sign is not a number
    assert parse_guess("-") == (False, None, "That is not a number.")

def test_decimal_numbers():
    # Decimals are truncated toward zero
    assert parse_guess("3.0") == (True, 3, None)
    assert parse_guess("1.5") == (True, 1, None)
    assert parse_guess("-7.9") == (True, -7, None)
    assert parse_guess(".5") == (True, 0, None)
    assert parse_guess("5.") == (True, 5, None)
    # More than one decimal point is not a number
    assert parse_guess("1.2.3") == (False, None, "That is not a number.")
