"""Test Bracket Behaviour"""

from calculator import calculator

# Nested Parentheses and Braces with Negative Numbers
def test_nested_parentheses_and_braces():
    output = calculator("(({4 + -5} * (2 + 3)) - 6) / 2; q")
    assert output == ["-5.5"]


# Complex Expressions and Chained Calculations
def test_complex_expressions_and_chained_calculations():
    assert calculator("1 + 2; 14 * {3 + (-7 + 5)}; q") == ["3", "14"]
    assert calculator("2 + 2 3 * 3 200 * { 17 - (2 * 9 - 1)}; q") == [
        "4",
        "9",
        "0",
    ]
    


# Parentheses and Braces Handling
def test_parentheses_and_braces():
    assert calculator("17 * (42 - 10); q") == ["544"]
    assert calculator("14 * {3 + (-7 + 5)}; q") == ["14"]
    assert calculator("2 * (5 + 4; q") == [
        "Öffnende '(' ohne passende schließende ')'.",
    ]
    assert calculator("2 * ({5 + 4; q") == [
        "Öffnende '{' ohne passende schließende '}'.",
    ]


def test_imbalanced_nested_brackets():
    assert calculator("((2 + 3) * 4; q") == ["Öffnende '(' ohne passende schließende ')'."]
    assert calculator("{(4 + 5) * 2; q") == ["Öffnende '{' ohne passende schließende '}'."]
    assert calculator("((2 + {3 - 1}) * 4; q") == ["Öffnende '(' ohne passende schließende ')'."]

def test_correctly_nested_brackets():
    assert calculator("((2 + 3) * (4 - 1)); q") == ["15"]
    assert calculator("{4 * (2 + 3)} - 1; q") == ["19"]
    assert calculator("{(4 - {2 + 1}) * 3}; q") == ["3"]


def test_unnecessary_brackets():
    assert calculator("(((2 + 3))); q") == ["5"]
    assert calculator("{4 + {3 + {2 + 1}}}; q") == ["10"]
    assert calculator("2 * (3) + {4}; q") == ["10"]

def test_brackets_with_complex_operations():
    assert calculator("({4 * (3 - 2)} / {(7 + 3) - 5}); q") == ["0.8"]
    assert calculator("((2 + 3) * {4 - 2}) / 2; q") == ["5"]
    assert calculator("((10 / {5 - 3}) - 1) * 2; q") == ["8"]

def test_expressions_with_redundant_parentheses_and_brackets():
    assert calculator("(((5 + 3))) * 2; q") == ["16"]
    assert calculator("{(4)} + {(3)}; q") == ["7"]
