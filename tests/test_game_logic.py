import pytest
from logic_utils import check_guess, update_score, parse_guess, get_range_for_difficulty


# --- Bug: check_guess returned backward hint messages ---
# Too High said "Go HIGHER" and Too Low said "Go LOWER"

class TestCheckGuess:
    def test_correct_guess_returns_win(self):
        outcome, _ = check_guess(50, 50)
        assert outcome == "Win"

    def test_correct_guess_message(self):
        _, message = check_guess(50, 50)
        assert "Correct" in message

    def test_high_guess_outcome(self):
        outcome, _ = check_guess(80, 50)
        assert outcome == "Too High"

    def test_high_guess_hint_says_lower(self):
        # Bug: hint previously said GO HIGHER when guess was above secret
        _, message = check_guess(80, 50)
        assert "LOWER" in message

    def test_low_guess_outcome(self):
        outcome, _ = check_guess(20, 50)
        assert outcome == "Too Low"

    def test_low_guess_hint_says_higher(self):
        # Bug: hint previously said GO LOWER when guess was below secret
        _, message = check_guess(20, 50)
        assert "HIGHER" in message

    def test_one_above_secret(self):
        outcome, message = check_guess(51, 50)
        assert outcome == "Too High"
        assert "LOWER" in message

    def test_one_below_secret(self):
        outcome, message = check_guess(49, 50)
        assert outcome == "Too Low"
        assert "HIGHER" in message

    def test_win_at_minimum_boundary(self):
        outcome, _ = check_guess(1, 1)
        assert outcome == "Win"

    def test_win_at_maximum_boundary(self):
        outcome, _ = check_guess(100, 100)
        assert outcome == "Win"

    def test_integer_comparison_not_lexicographic(self):
        # Bug: secret was sometimes cast to str, causing wrong comparisons
        # e.g. str(9) > str(50) is True lexicographically, but 9 < 50 numerically
        outcome, _ = check_guess(9, 50)
        assert outcome == "Too Low"

    def test_large_guess_above_secret(self):
        outcome, message = check_guess(99, 1)
        assert outcome == "Too High"
        assert "LOWER" in message


# --- Bug: update_score deducted different amounts for Too High vs Too Low ---

class TestUpdateScore:
    def test_too_high_deducts_five(self):
        assert update_score(100, "Too High", 1) == 95

    def test_too_low_deducts_five(self):
        assert update_score(100, "Too Low", 1) == 95

    def test_too_high_and_too_low_deduct_same_amount(self):
        # Bug: one outcome deducted a different amount than the other
        assert update_score(100, "Too High", 1) == update_score(100, "Too Low", 1)

    def test_penalty_applies_from_zero(self):
        assert update_score(0, "Too High", 1) == -5

    def test_penalty_applies_from_negative(self):
        assert update_score(-5, "Too Low", 1) == -10

    def test_win_first_attempt_score(self):
        # attempts initialized to 0, incremented before call → attempt_number=1
        # points = 100 - 10*(1+1) = 80
        assert update_score(0, "Win", 1) == 80

    def test_win_later_attempt_gives_fewer_points(self):
        # attempt_number=5: 100 - 10*6 = 40
        assert update_score(0, "Win", 5) == 40

    def test_win_score_floored_at_ten_points(self):
        # Bug (off-by-one): if attempts started at 1, attempt_number would be inflated,
        # hitting the floor sooner and awarding fewer points than earned
        # attempt_number=10: 100 - 110 = -10 → clamped to 10
        assert update_score(0, "Win", 10) == 10

    def test_win_adds_to_existing_score(self):
        assert update_score(50, "Win", 1) == 130

    def test_off_by_one_attempt_costs_points(self):
        # Bug: attempts init to 1 meant first win used attempt_number=2 not 1
        correct_first_win = update_score(0, "Win", 1)
        off_by_one_first_win = update_score(0, "Win", 2)
        assert correct_first_win > off_by_one_first_win

    def test_unknown_outcome_unchanged(self):
        assert update_score(50, "Unknown", 1) == 50


# --- parse_guess edge cases ---

class TestParseGuess:
    def test_none_returns_error(self):
        ok, val, err = parse_guess(None)
        assert not ok and val is None and err is not None

    def test_empty_string_returns_error(self):
        ok, _, _ = parse_guess("")
        assert not ok

    def test_valid_integer(self):
        ok, val, err = parse_guess("42")
        assert ok and val == 42 and err is None

    def test_float_string_truncates(self):
        ok, val, _ = parse_guess("3.7")
        assert ok and val == 3

    def test_float_dot_zero(self):
        ok, val, _ = parse_guess("5.0")
        assert ok and val == 5

    def test_non_numeric_returns_error(self):
        ok, _, err = parse_guess("abc")
        assert not ok and err is not None

    def test_whitespace_returns_error(self):
        ok, _, _ = parse_guess("   ")
        assert not ok

    def test_negative_number(self):
        ok, val, _ = parse_guess("-5")
        assert ok and val == -5


# --- get_range_for_difficulty ---

class TestGetRangeForDifficulty:
    def test_easy_range(self):
        assert get_range_for_difficulty("Easy") == (1, 20)

    def test_normal_range(self):
        assert get_range_for_difficulty("Normal") == (1, 100)

    def test_hard_range(self):
        assert get_range_for_difficulty("Hard") == (1, 50)

    def test_unknown_defaults_to_normal(self):
        assert get_range_for_difficulty("Unknown") == (1, 100)
