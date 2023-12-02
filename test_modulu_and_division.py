"""test_modulu_and_division"""
from calculator import calculator

# Sequential Commands After Error
def test_sequential_commands_after_error():
    output = calculator("42 / 0; 1 + 1; q")
    assert output == ["Division durch 0 ist nicht erlaubt.", "2"]


# Division of Zero by Any Number
def test_division_of_zero_by_any_number():
    output = calculator("0 / 42; q")
    assert output == ["0"]


# Division by Zero and Modulo Operations
def test_division_by_zero_and_modulo():
    assert calculator("42 - 17 / 0; q") == [
        "Division durch 0 ist nicht erlaubt.",
    ]
    assert calculator("42 - 17 / (2.5-1.25-1.25); q") == [
        "Division durch 0 ist nicht erlaubt.",
    ]
    assert calculator("42 - 17 % 0; q") == [
        "Modulo durch 0 ist nicht erlaubt.",
    ]
    assert calculator("42 - 17 % (2.5-1.25-1.25); q") == [
        "Modulo durch 0 ist nicht erlaubt.",
    ]
    assert calculator("18.3 % 5; q") == [
        "Modulo ist nur auf ganzen Zahlen erlaubt.",
    ]
    assert calculator("18 % 5.3; q") == [
        "Modulo ist nur auf ganzen Zahlen erlaubt.",
    ]
    assert calculator("17 % 4; q") == ["1"]



def test_basic_division_and_modulo():
    assert calculator("10 / 2; q") == ["5"]
    assert calculator("-10 / 2; q") == ["-5"]
    assert calculator("10 % 3; q") == ["1"]
    assert calculator("-10 % 3; q") == ["-1"]


def test_division_by_zero():
    assert calculator("1 / 0; q") == ["Division durch 0 ist nicht erlaubt."]
    assert calculator("-5 / 0; q") == ["Division durch 0 ist nicht erlaubt."]


def test_modulo_special_cases():
    assert calculator("5 % 0; q") == ["Modulo durch 0 ist nicht erlaubt."]
    assert calculator("5.5 % 2; q") == ["Modulo ist nur auf ganzen Zahlen erlaubt."]
    assert calculator("5 % 2.5; q") == ["Modulo ist nur auf ganzen Zahlen erlaubt."]


def test_combined_division_and_modulo():
    assert calculator("10 / 2 + 3 % 1; q") == ["5"]
    assert calculator("(15 % 4) / 2; q") == ["1.5"]
    assert calculator("20 / (6 % 2); q") == ["Division durch 0 ist nicht erlaubt."]

def test_division_and_modulo_with_negative_numbers():
    assert calculator("-10 / 2; q") == ["-5"]
    assert calculator("10 % -3; q") == ["1"]
    assert calculator("-10 % 3; q") == ["-1"]
