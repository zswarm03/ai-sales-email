from flask import Flask, render_template, request, jsonify
from email_generator import generate_sales_email

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate-email", methods=["POST"])
def generate_email():
    data = request.get_json()
    name = data.get("name")
    product = data.get("product")
    behavior = data.get("behavior")

    if not name or not product or not behavior:
        return jsonify({"error": "Missing input fields"}), 400

    personalized_email = generate_sales_email(name, product, behavior)
    
    return jsonify({"email": personalized_email})

if __name__ == "__main__":
    app.run(debug=True)

