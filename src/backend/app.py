from flask import Flask, jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

teamsdata = [
    {
        "id": 1,
        "name": "Konveyor",
        "members": ["Ethan", "Xavier", "Paris"],
        "score": "N/A"
    },
    {
        "id": 2,
        "name": "Example",
        "members": ["Deven", "Jeff"],
        "score": "N/A"
    }
]

@app.route('/teamdata', methods=['GET'])
def get_teams():
    return jsonify(teamsdata)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
