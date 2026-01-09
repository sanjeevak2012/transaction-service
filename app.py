from flask import Flask

app = Flask(__name__)   # 👈 MUST be first

@app.route("/")
def home():
    return "Transaction Service is running"

@app.route("/transaction")
def transaction():
    return "Transaction endpoint"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
