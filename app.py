from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return "hello pintu welcome to mad 1 project"


if __name__ == "__main__":
    app.run(debug=True)




