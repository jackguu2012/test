from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index_simple.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.form.get("user_message")
    # You can customize the responses directly in the HTML file
    response = get_custom_response(user_message)
    return str(response)

def get_custom_response(user_message):
    # Add your custom responses here
    if "hello" in user_message.lower():
        return "Hi there!"
    elif "how are you" in user_message.lower():
        return "I'm doing well, thank you!"
    else:
        return "I didn't understand that. Can you ask something else?"

if __name__ == "__main__":
    app.run(debug=True)