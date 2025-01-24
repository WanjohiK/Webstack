# Python (Flask back-end)
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# Sample database (replace with a real database)
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_result', methods=['POST'])
def save_result():
    data = request.json
    username = data['username']
    score = data['score']
    users[username] = score
    return jsonify({"message": "Result saved successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
