from flask import Flask, render_template

# Initialize the Flask app
app = Flask(__name__)


# Define the route for the homepage
@app.route("/")
def home():
    # Render the HTML template and pass a message
    return render_template("index.html", message="Hello and welcome to CSE Workshop!")


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
