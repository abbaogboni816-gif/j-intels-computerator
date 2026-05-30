"""
Professional Calculator Module

This module provides comprehensive mathematical operations including:
- Basic arithmetic (add, subtract, multiply, divide, modulus)
- Advanced functions (square root)
- Algebraic operations (solve equations, differentiation, integration)

Supports symbolic mathematics through SymPy for advanced calculations.
All functions include proper error handling and validation.

Author: J-Intels
Version: 2.0 - Professional Edition
"""

import math
from sympy import symbols, solve, diff, integrate
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor,
)


TRANSFORMATIONS = standard_transformations + (
    implicit_multiplication_application,
    convert_xor,
)


def _parse_expression(expression, local_dict):
    """Parse user-friendly math syntax into a SymPy expression."""
    return parse_expr(
        expression,
        transformations=TRANSFORMATIONS,
        local_dict=local_dict,
    )


def _normalize_equation(expression):
    """Convert equations with '=' into an expression equal to zero."""
    if "=" not in expression:
        return expression

    left, right = expression.split("=", 1)
    if not left.strip() or not right.strip():
        raise ValueError("Equation must have values on both sides of '='")

    return f"({left}) - ({right})"


def add(a, b):
    """Add two numbers and return the result."""
    return a + b


def subtract(a, b):
    """Subtract two numbers and return the result."""
    return a - b


def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b


def divide(a, b):
    """Divide two numbers and return the result."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def find_modulus(a, b):
    """Find the modulus of two numbers and return the result."""
    if b == 0:
        raise ValueError("Cannot find modulus with zero")
    return a % b


def find_square_root(a):
    """Calculate the square root of a number and return the result."""
    if a < 0:
        raise ValueError("Cannot find square root of negative number")
    return math.sqrt(a)


def solve_algebra(expression):
    """
    Solve an algebraic equation for x.
    
    Takes an expression as input like "2*x + 5 - 15" or "(x+3)(x-3)"
    Supports implicit multiplication like (x+3)(x-3) which equals x^2 - 9.
    Uses symbols to create x, parse_expr to convert the expression,
    and solve to find the solution.
    
    Args:
        expression (str): A mathematical expression containing x
        
    Returns:
        list: Solutions for x in the equation
        
    Raises:
        ValueError: If the expression is invalid or cannot be solved
    """
    try:
        x = symbols('x')
        expression = _normalize_equation(expression)
        expr = _parse_expression(expression, {'x': x})
        result = solve(expr, x)
        return result
    except Exception as e:
        raise ValueError(f"Invalid expression: {str(e)}")


def differentiate(expression, variable='x'):
    """
    Calculate the derivative of an expression.
    
    Takes an expression as input like "x**2 + 3*x + 2" or "(x+3)(x-3)"
    Supports implicit multiplication.
    Returns its derivative with respect to the specified variable.
    
    Args:
        expression (str): A mathematical expression
        variable (str): The variable to differentiate with respect to (default: 'x')
        
    Returns:
        str: The derivative of the expression
        
    Raises:
        ValueError: If the expression is invalid
    """
    try:
        var = symbols(variable)
        expr = _parse_expression(expression, {variable: var})
        derivative = diff(expr, var)
        return str(derivative)
    except Exception as e:
        raise ValueError(f"Invalid expression: {str(e)}")


def integrate_expression(expression, variable='x'):
    """
    Calculate the indefinite integral of an expression.
    
    Takes an expression as input like "x**2 + 3*x + 2" or "(x+3)(x-3)"
    Supports implicit multiplication.
    Returns its indefinite integral with respect to the specified variable.
    
    Args:
        expression (str): A mathematical expression
        variable (str): The variable to integrate with respect to (default: 'x')
        
    Returns:
        str: The indefinite integral of the expression (without constant)
        
    Raises:
        ValueError: If the expression is invalid
    """
    try:
        var = symbols(variable)
        expr = _parse_expression(expression, {variable: var})
        integral = integrate(expr, var)
        return str(integral)
    except Exception as e:
        raise ValueError(f"Invalid expression: {str(e)}")


def main():
    """Main function to run the calculator."""
    print("=" * 60)
    print("Welcome to Professional Calculator!")
    print("=" * 60)
    print("\nAvailable operations:")
    print("  • Basic: add, subtract, multiply, divide, modulus, square root")
    print("  • Algebra: solve, differentiate, integrate")
    print("  • Example: Type 'solve' for solving equations like (x+3)(x-3)=0")
    print("\nOr enter an expression directly and we'll detect the operation!")
    print("=" * 60)

    user_input = input("\nEnter operation or expression: ").strip().lower()
    
    try:
        # Check if user input contains algebra-specific patterns
        has_x = 'x' in user_input
        has_parentheses = '(' in user_input and ')' in user_input
        has_equals = '=' in user_input
        
        # Auto-detect algebra operations
        if has_equals and has_x:
            # Solve equation
            expression = user_input.replace('=', '-')
            print(f"\nSolving: {user_input}")
            result = solve_algebra(expression)
            print(f"Result: {result}")
        elif (has_parentheses or has_x) and user_input in ["solve", "algebra", "equation"]:
            # User explicitly asked to solve
            expression = input("Enter the equation (e.g., '(x+3)(x-3) = 0' or just '(x+3)(x-3)'): ").strip()
            expression = expression.replace('=', '-') if '=' in expression else expression
            print(f"\nSolving: {expression}")
            result = solve_algebra(expression)
            print(f"Result: {result}")
        elif user_input == "square root":
            number = float(input("Enter the number: "))
            result = find_square_root(number)
            print(f"\nResult: {result}")
        elif user_input == "differentiate" or user_input == "derivative":
            expression = input("Enter the expression (e.g., 'x**2 + 3*x + 2' or '(x+3)(x-3)'): ").strip()
            variable = input("Enter the variable (default 'x'): ").strip() or 'x'
            print(f"\nDerivative of {expression}:")
            result = differentiate(expression, variable)
            print(f"Result: {result}")
        elif user_input == "integrate" or user_input == "integral":
            expression = input("Enter the expression (e.g., 'x**2 + 3*x + 2' or '(x+3)(x-3)'): ").strip()
            variable = input("Enter the variable (default 'x'): ").strip() or 'x'
            print(f"\nIntegral of {expression}:")
            result = integrate_expression(expression, variable)
            print(f"Result: {result}")
        elif user_input in ["add", "subtract", "multiply", "divide", "modulus"]:
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))
            
            if user_input == "add":
                result = add(number1, number2)
            elif user_input == "subtract":
                result = subtract(number1, number2)
            elif user_input == "multiply":
                result = multiply(number1, number2)
            elif user_input == "divide":
                result = divide(number1, number2)
            elif user_input == "modulus":
                result = find_modulus(number1, number2)
            
            print(f"\nResult: {result}")
        else:
            # Try to interpret as a math expression or basic operation
            if user_input.replace('.', '', 1).replace('-', '', 1).isdigit():
                print("Error: Please enter a valid operation or expression.")
            else:
                print("Error: Invalid operation. Please try again.")
                print("Valid operations: add, subtract, multiply, divide, modulus, square root")
                print("                 solve, differentiate, integrate")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\n" + "=" * 60)
        print("Thank you for using Calculator!")
        print("=" * 60)


if __name__ == "__main__":
    main()
