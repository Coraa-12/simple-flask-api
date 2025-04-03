# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from my Flask App in WSL!"})

# ---> ADD THIS NEW ROUTE <---
@app.route('/ping')
def ping():
    # A simple health check / keep-alive endpoint
    return jsonify({"response": "pong"})
# ---> END OF NEW ROUTE <---

# This block allows running the app directly using `python app.py`
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)