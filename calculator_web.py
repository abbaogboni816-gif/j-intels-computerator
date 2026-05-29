"""
Calculator Web Application

A Flask-based web interface for the calculator module.
Provides a web UI for performing basic arithmetic operations.
"""

from flask import Flask, render_template, request, jsonify
import calculator


app = Flask(__name__)


@app.route("/")
def home():
    """Render the calculator home page."""
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    """Handle calculation requests from the web UI."""
    data = request.json
    operation = data.get("operation")

    # Validate that operation is provided
    if operation is None:
        return jsonify({"error": "Missing required field: operation."}), 400

    try:
        # Handle algebra operations (differentiate, integrate, solve)
        if operation == "differentiate":
            expression = data.get("expression")
            variable = data.get("variable", 'x')
            
            if not expression:
                return jsonify({"error": "Missing required field: expression."}), 400
            
            result = calculator.differentiate(expression, variable)
            return jsonify({"result": result})
        
        elif operation == "integrate":
            expression = data.get("expression")
            variable = data.get("variable", 'x')
            
            if not expression:
                return jsonify({"error": "Missing required field: expression."}), 400
            
            result = calculator.integrate_expression(expression, variable)
            return jsonify({"result": result})
        
        elif operation == "solve":
            expression = data.get("expression")
            
            if not expression:
                return jsonify({"error": "Missing required field: expression."}), 400
            
            result = calculator.solve_algebra(expression)
            return jsonify({"result": result})
        
        # Handle basic arithmetic operations
        else:
            num1 = data.get("num1")
            num2 = data.get("num2")
            
            # Validate required fields for arithmetic operations
            if operation == "sqrt":
                if num1 is None:
                    return jsonify({"error": "Missing required field: num1."}), 400
                
                try:
                    num1 = float(num1)
                except ValueError:
                    return jsonify({"error": "Invalid input. Please enter a numeric value."}), 400
                
                result = calculator.find_square_root(num1)
                return jsonify({"result": result})
            
            elif operation in ["add", "subtract", "multiply", "divide", "modulus"]:
                if num1 is None or num2 is None:
                    return jsonify({"error": "Missing required fields: num1, num2."}), 400
                
                try:
                    num1 = float(num1)
                    num2 = float(num2)
                except ValueError:
                    return jsonify({"error": "Invalid input. Please enter numeric values."}), 400
                
                if operation == "add":
                    result = calculator.add(num1, num2)
                elif operation == "subtract":
                    result = calculator.subtract(num1, num2)
                elif operation == "multiply":
                    result = calculator.multiply(num1, num2)
                elif operation == "divide":
                    try:
                        result = calculator.divide(num1, num2)
                    except ValueError as e:
                        return jsonify({"error": str(e)}), 400
                elif operation == "modulus":
                    try:
                        result = calculator.find_modulus(num1, num2)
                    except ValueError as e:
                        return jsonify({"error": str(e)}), 400
                
                return jsonify({"result": result})
            
            else:
                return jsonify({"error": f"Invalid operation: {operation}"}), 400
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)
