from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)


def getconnection():
    try:
        con = psycopg2.connect(database="neondb", user='neondb_owner', password='npg_hF0MHjSXNeu5', 
                               host='ep-red-band-a4ckcbjp-pooler.us-east-1.aws.neon.tech', port= '5432')
        return con
    except Exception as e:
        return None

@app.route('/teams', methods=['GET'])
def getteams():
    connection = getconnection()
    if not connection:
        return jsonify({"error": "Could not to connect to database"}), 500

    try:
        curs = connection.cursor()
        curs.execute("SELECT id, name, teamcategory, totalscore, scores FROM \"Teams\";")
        rows = curs.fetchall()
        teams = [
            {
                "id": row[0],
                "name": row[1],
                "teamcategory": row[2],
                "scores": row[3],
                "totalscore": row[4]
            }
            for row in rows
        ]
        return jsonify(teams)
    except Exception as e:
        return jsonify({"error": f"Failed to fetch team data: {str(e)}"}), 500
    finally:
        curs.close()
        connection.close()


if __name__ == '__main__':
    app.run(debug=True, port=5000)