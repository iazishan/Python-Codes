from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_response(user_input):
    user_input = user_input.lower()
    if "shirt" in user_input or "t-shirt" in user_input:
        return "We have a variety of shirts and t-shirts in different sizes and colors. Would you like to see our latest collection?"
    elif "jeans" in user_input or "pants" in user_input:
        return "Our jeans and pants are available in all sizes. Do you prefer slim fit or regular fit?"
    elif "dress" in user_input:
        return "We offer dresses for all occasions. Are you looking for casual or formal dresses?"
    elif "price" in user_input or "cost" in user_input:
        return "Please specify the item you want the price for."
    elif "return" in user_input or "exchange" in user_input:
        return "You can return or exchange items within 30 days of purchase. Would you like to know more about our policy?"
    elif "bye" in user_input:
        return "Thank you for visiting! Have a great day!"
    else:
        return "I'm here to help with any questions about our clothing and accessories. Please ask me anything!"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
