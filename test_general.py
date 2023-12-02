"""General tests"""

from calculator import calculator


# Nested Operations Without Quitting
def test_chained_operations_without_quitting():
    output = calculator("4 + 5; 6*7; q")
    assert output == ["9", "42"]


# Basic Arithmetic Operations
def test_basic_arithmetic_operations():
    assert calculator("4 * 7 - 3 / 5 + 7; q") == ["34.4"]
    assert calculator("2 - 3 * 5; q") == ["-13"]
    assert calculator("14 + -4; q") == ["10"]



# Error Handling and Edge Cases
def test_error_handling_and_edge_cases():
    assert calculator("3**2; q") == ["Primärausdruck erwartet"]
    assert calculator("3@5; q") == ["Falsches Token"]
    assert calculator("let let = 3; q") == [
        "Bezeichner erwartet in Deklaration.",
    ]
    

def test_negative_numbers_and_unconventional_syntax():
    assert calculator("14 + --4; q") == ["18"]
    assert calculator("-5 * 4; q") == ["-20"]
    assert calculator("+-+-3; q") == ["3"]
    assert calculator("4 - -3; q") == ["7"]


def test_sequential_operations_with_variables():
    assert calculator("let a = 4; a + 5; a * 2; q") == ["4", "9", "8"]
    assert calculator("let b = 3; 2 * b - 1; b / 2; q") == ["3", "5", "1.5"]

def test_complex_expressions_with_mixed_operators():
    assert calculator("2 + 3 * 5 - 4 / 2; q") == ["15"]
    assert calculator("3 - 2 + 4 * 5 / 2; q") == ["11"]
