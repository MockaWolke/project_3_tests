"""Test Variable and Constants"""

# Assuming the calculator function is defined in another file named 'calculator_module.py'
from calculator import calculator

# Variable Declaration and Assignment
def test_variable_declaration_and_assignment():
    assert calculator("let var1 = 7.2; let var2 = 3.1; 3 * { var1 - var2 * 2}; q") == [
        "7.2",
        "3.1",
        "3",
    ]
    assert calculator("set var1 = 7.2; q") == [
        "Diese Variable ist undefiniert.",
    ]
    assert calculator("let var1 = 1; let var1 = 1; q") == [
        "1",
        "Variable bereits deklariert.",
    ]

# Incorrect Syntax for Variable Declaration and Assignment
def test_incorrect_syntax_for_variable_declaration():
    output = calculator("let x 5; q")
    assert output == ["'=' fehlt in Deklaration."]
    
    output = calculator("let x= 5; set x 5;set x; q")
    assert output == ["5","'=' fehlt in Zuordnung.","'=' fehlt in Zuordnung."]
    
    

# Use of the Modulo Operator with Variables and Constants
def test_modulo_with_variables_and_constants():
    output = calculator(r"let a = 10; let b = 3; a % b; let c = pi; c % 2; q")
    assert output == [
        "10",
        "3",
        "1",
        "3.14159",
        "Modulo ist nur auf ganzen Zahlen erlaubt.",
    ]
    
    
# Reassignment of Variables to Different Types
def test_reassignment_of_variables_to_different_types():
    output = calculator("let a = 5; set a = 5.5; q")
    assert output == ["5", "5.5"]
    
# Expressions Involving Unassigned Variables
def test_expressions_involving_unassigned_variables():
    output = calculator("a * 2; q")
    assert output == ["Diese Variable ist undefiniert."]





def test_assigning_new_value_to_constant_pi():
    output = calculator("set pi = 3; q")
    assert output == ["Konstanten sind nicht veränderbar."]


# Attempting to assign a new value to the constant 'e'
def test_assigning_new_value_to_constant_e():
    output = calculator("set e = 2; q")
    assert output == ["Konstanten sind nicht veränderbar."]


# Multiple Variable Declarations and Calculations
def test_multiple_variable_declarations_and_calculations():
    output = calculator(
        "let a = 5; let b = a + 3; set a = b; let c = a * b; set c = c / (a * 2); q"
    )
    assert output == ["5", "8", "8", "64", "4"]


def test_alphanumeric_variable_names():
    assert calculator("let var123 = 10; var123 * 2; q") == ["10", "20"]
    assert calculator("let a1b2 = 5; set a1b2 = a1b2 + 3; a1b2; q") == ["5", "8", "8"]


def test_spaces_before_operators():
    assert calculator("let a=5 ; a + 2; q") == ["5", "7"]
    assert calculator("let a= 5; set a= 10 ; a * 3; q") == ["5", "10", "30"]


def test_complex_variable_manipulations():
    assert calculator("let x = 2; let y = x * 3; let z = y + x; z; q") == ["2", "6", "8", "8"]
    assert calculator("let num1 = 10; let num2 = num1 + 5; set num1 = num2; num1 * num2; q") == ["10", "15", "15", "225"]

def test_variable_name_edge_cases():
    assert calculator("let piVar = 3.14; piVar * 2; q") == ["3.14", "6.28"]
    assert calculator("let setVar = 5; setVar + 3; q") == ["5", "8"]


def test_variables_in_complex_expressions():
    assert calculator("let a = 5; let b = 2; (a + b) * (a - b); q") == ["5", "2", "21"]
    assert calculator("let x = 7; let y = 3; x*x - 2*x*y + y*y; q") == ["7", "3", "16"]
