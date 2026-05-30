"""
Professional Calculator Web Application

A Flask-based REST API providing web and browser interfaces for the J-Intels Calculator.
Serves both the web UI (HTML/CSS/JavaScript) and programmatic API endpoints.

Features:
- RESTful API for all calculator operations
- Web UI with responsive, professional design
- Support for basic arithmetic and advanced algebra operations
- Comprehensive error handling and validation
- JSON-based request/response format

Author: J-Intels
Version: 2.0 - Professional Edition
"""

from flask import Flask, render_template, request, jsonify
import calculator
from pyngrok import ngrok


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
            # Convert result to list of strings for JSON serialization
            result = [str(r) for r in result] if isinstance(result, list) else str(result)
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
    # Set host to 0.0.0.0 to allow access from other devices on the network
    # Access from this computer: http://localhost:5000
    # Access from other devices: http://<your-ip>:5000 or http://<computer-name>:5000
    
    print("\n" + "="*60)
    print("J-INTELS CALCULATOR - STARTING SERVER")
    print("="*60)
    
    try:
        # Create ngrok tunnel for public internet access
        public_url = ngrok.connect(5000)
        print(f"\n✅ PUBLIC URL (Access from ANYWHERE): {public_url}")
        print(f"   Share this link with anyone on the internet!\n")
    except Exception as e:
        print(f"\n⚠️  Could not create public URL: {e}")
        print("   But local network access still works!\n")
    
    print(f"✅ LOCAL NETWORK URL: http://<your-ip>:5000")
    print(f"   (Replace <your-ip> with your computer's IP address)\n")
    print(f"✅ LOCAL COMPUTER URL: http://localhost:5000\n")
    print("="*60)
    print("Press CTRL+C to stop the server")
    print("="*60 + "\n")
    
    app.run(debug=True, host="0.0.0.0", port=5000, use_reloader=False)
