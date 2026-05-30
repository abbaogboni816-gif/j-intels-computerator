# J-Intels Calculator - Professional Edition

A comprehensive, production-ready calculator application with multiple interfaces: Web UI, GUI, and Python API.

## Features

### Core Capabilities
- **Basic Arithmetic**: Addition, subtraction, multiplication, division, modulus
- **Advanced Math**: Square root, trigonometric functions (sin, cos, tan), π constant
- **Algebra**: Solve equations, differentiation, integration
- **Symbolic Math**: Support for implicit multiplication, complex expressions

### Interfaces
1. **Web Application** - Professional, responsive browser interface
2. **GUI Application** - Tkinter-based desktop calculator
3. **Python API** - Programmatic access to all functions

## Project Structure

```
calculator_project/
├── calculator.py              # Core mathematical operations
├── calculator_web.py          # Flask web server and REST API
├── calculator_gui.py          # Tkinter GUI application
├── templates/
│   └── index.html            # Professional web interface
└── README.md                 # This file
```

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Required Dependencies
```bash
pip install flask sympy
```

## Usage

### Option 1: Web Application (Recommended)

1. Start the Flask server:
```bash
python calculator_web.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

3. Use the professional interface to perform calculations

### Option 2: GUI Application

Run the Tkinter application:
```bash
python calculator_gui.py
```

Features:
- Click buttons for intuitive input
- Supports basic operations (+, -, ×, ÷, %)
- Square root function
- Trigonometric functions (sin, cos, tan)
- Constants (π)
- Backspace and Clear buttons
- Color-coded buttons for different operation types

### Option 3: Python API

Import and use directly in your Python code:

```python
from calculator import add, subtract, multiply, divide, find_square_root
from calculator import solve_algebra, differentiate, integrate_expression

# Basic operations
result = add(10, 5)              # Returns: 15
result = multiply(4, 3)          # Returns: 12
result = find_square_root(16)   # Returns: 4.0

# Algebra operations
solutions = solve_algebra("x**2 - 4")           # Returns: [-2, 2]
derivative = differentiate("x**2 + 3*x + 2")    # Returns: 2*x + 3
integral = integrate_expression("x**2")         # Returns: x**3/3
```

## API Endpoints (Web Application)

### POST /calculate
Performs any supported calculation operation.

**Request Format:**
```json
{
  "operation": "add",
  "num1": 10,
  "num2": 5
}
```

**Supported Operations:**
- `add` - Addition (requires: num1, num2)
- `subtract` - Subtraction (requires: num1, num2)
- `multiply` - Multiplication (requires: num1, num2)
- `divide` - Division (requires: num1, num2)
- `modulus` - Modulus (requires: num1, num2)
- `sqrt` - Square Root (requires: num1)
- `differentiate` - Derivative (requires: expression, optional: variable)
- `integrate` - Integral (requires: expression, optional: variable)
- `solve` - Solve Equation (requires: expression)

**Response Format:**
```json
{
  "result": 15
}
```

**Error Response:**
```json
{
  "error": "Error message describing what went wrong"
}
```

## Examples

### Web Application Examples

#### Example 1: Add two numbers
1. Select: "Add"
2. Input: 25 and 15
3. Click: "Calculate"
4. Result: 40

#### Example 2: Solve an equation
1. Select: "Solve Equation"
2. Input: "x**2 - 9"
3. Click: "Calculate"
4. Result: [-3, 3]

#### Example 3: Differentiate
1. Select: "Differentiate"
2. Input: "x**3 + 2*x**2 + x"
3. Variable: x (default)
4. Click: "Calculate"
5. Result: 3*x**2 + 4*x + 1

### GUI Calculator Examples

#### Example 1: Simple Addition
1. Click: 5 + 3
2. Click: =
3. Result: 8

#### Example 2: Sine of 45 degrees
1. Click: 45
2. Click: sin
3. Result: 0.7071067812

#### Example 3: Square Root
1. Click: 144
2. Click: √
3. Result: 12

## Configuration

### Web Application Settings
Edit `calculator_web.py` to modify:
- **Host**: Change `localhost` to `0.0.0.0` for network access
- **Port**: Change `5000` to any available port
- **Debug Mode**: Set `debug=False` for production

```python
if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)
```

### GUI Application Settings
Edit `calculator_gui.py` to modify:
- **Window Size**: Adjust `window.geometry("500x650")`
- **Theme Colors**: Modify the color configuration variables
- **Button Layout**: Add or remove buttons from the `buttons` array

## Error Handling

All operations include comprehensive error handling:
- **Division by Zero**: Returns error message
- **Invalid Input**: Validates numeric input before processing
- **Invalid Expressions**: Provides feedback for malformed expressions
- **Negative Square Root**: Returns appropriate error

## Performance

- Lightweight and fast for typical calculations
- Handles complex symbolic mathematics efficiently
- Web interface requires minimal bandwidth
- GUI runs smoothly on all modern systems

## Security Notes

- Input validation prevents code injection
- Web server uses JSON serialization
- No sensitive data is stored
- CORS not enabled by default (local only)

## Troubleshooting

### Web Application Won't Start
- Ensure Port 5000 is not in use: `netstat -ano | findstr :5000`
- Check Flask is installed: `pip install flask`
- Verify Python version: `python --version`

### GUI Application Won't Open
- Ensure tkinter is installed
- On Linux: `sudo apt-get install python3-tk`
- On macOS: Included with Python

### Import Errors
- Install SymPy: `pip install sympy`
- Verify all files are in the same directory

## Version History

### Version 2.0 (Professional Edition)
- Completely redesigned web interface
- Professional GUI with color-coded buttons
- Enhanced error handling and validation
- Improved documentation
- Fixed JavaScript template interpolation issues
- Proper HTML structure and semantics

### Version 1.0
- Initial release with basic calculator functions

## Support

For issues or questions:
1. Check this README
2. Verify all dependencies are installed
3. Review error messages carefully
4. Ensure correct input format

## License

Professional Edition - J-Intels

---

**Ready for production use.** All components tested and verified.
