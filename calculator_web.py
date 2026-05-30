"""
Professional Calculator Web Application

A Flask-based REST API providing web and browser interfaces for the J-Intels Calculator.
Serves both the web UI (HTML/CSS/JavaScript) and programmatic API endpoints.
"""

import calculator
from flask import Flask, jsonify, render_template, request

try:
    from pyngrok import ngrok
except ImportError:
    ngrok = None


app = Flask(__name__)


@app.route("/")
def home():
    """Render the calculator home page."""
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    """Handle calculation requests from the web UI."""
    data = request.get_json(silent=True) or {}
    operation = data.get("operation")

    if operation is None:
        return jsonify({"error": "Missing required field: operation."}), 400

    try:
        if operation == "differentiate":
            expression = data.get("expression")
            variable = data.get("variable", "x")

            if not expression:
                return jsonify({"error": "Missing required field: expression."}), 400

            result = calculator.differentiate(expression, variable)
            return jsonify({"result": result})

        if operation == "integrate":
            expression = data.get("expression")
            variable = data.get("variable", "x")

            if not expression:
                return jsonify({"error": "Missing required field: expression."}), 400

            result = calculator.integrate_expression(expression, variable)
            return jsonify({"result": result})

        if operation == "solve":
            expression = data.get("expression")

            if not expression:
                return jsonify({"error": "Missing required field: expression."}), 400

            result = calculator.solve_algebra(expression)
            result = [str(item) for item in result] if isinstance(result, list) else str(result)
            return jsonify({"result": result})

        num1 = data.get("num1")
        num2 = data.get("num2")

        if operation == "sqrt":
            if num1 is None:
                return jsonify({"error": "Missing required field: num1."}), 400

            try:
                num1 = float(num1)
            except (TypeError, ValueError):
                return jsonify({"error": "Invalid input. Please enter a numeric value."}), 400

            result = calculator.find_square_root(num1)
            return jsonify({"result": result})

        if operation in ["add", "subtract", "multiply", "divide", "modulus"]:
            if num1 is None or num2 is None:
                return jsonify({"error": "Missing required fields: num1, num2."}), 400

            try:
                num1 = float(num1)
                num2 = float(num2)
            except (TypeError, ValueError):
                return jsonify({"error": "Invalid input. Please enter numeric values."}), 400

            if operation == "add":
                result = calculator.add(num1, num2)
            elif operation == "subtract":
                result = calculator.subtract(num1, num2)
            elif operation == "multiply":
                result = calculator.multiply(num1, num2)
            elif operation == "divide":
                result = calculator.divide(num1, num2)
            else:
                result = calculator.find_modulus(num1, num2)

            return jsonify({"result": result})

        return jsonify({"error": f"Invalid operation: {operation}"}), 400

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("J-INTELS CALCULATOR - STARTING SERVER")
    print("=" * 60)

    if ngrok is not None:
        try:
            public_url = ngrok.connect(5000)
            print(f"\nPUBLIC URL (Access from ANYWHERE): {public_url}")
            print("   Share this link with anyone on the internet!\n")
        except Exception as e:
            print(f"\nCould not create public URL: {e}")
            print("   Local network access still works.\n")
    else:
        print("\npyngrok is not installed, so public URL sharing is disabled.")
        print("   Local network access still works.\n")

    print("LOCAL NETWORK URL: http://<your-ip>:5000")
    print("   (Replace <your-ip> with your computer's IP address)\n")
    print("LOCAL COMPUTER URL: http://localhost:5000\n")
    print("=" * 60)
    print("Press CTRL+C to stop the server")
    print("=" * 60 + "\n")

    app.run(debug=True, host="0.0.0.0", port=5000, use_reloader=False)
