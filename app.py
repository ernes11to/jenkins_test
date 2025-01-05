from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Dockerized Flask App modified to tests webhook!"

@app.route("/api")
def api():
    return {"message": "This is a simple API"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
