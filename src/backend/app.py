from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

def getconnection():
    try:
        con = psycopg2.connect(
            database="neondb",
            user='neondb_owner',
            password='npg_hF0MHjSXNeu5',
            host='ep-red-band-a4ckcbjp-pooler.us-east-1.aws.neon.tech',
            port='5432'
        )
        return con
    except Exception:
        return None


@app.route('/teams', methods=['GET'])
def getteams():
    connection = getconnection()
    if not connection:
        return jsonify({"error": "Could not connect to database"})

    try:
        curs = connection.cursor()
        curs.execute("SELECT id, name, teamcategory, totalscore, scores FROM \"Teams\";")
        rows = curs.fetchall()
        teams = [
            {
                "id": row[0],
                "name": row[1],
                "teamcategory": row[2],
                "totalscore": row[3],
                "scores": row[4]
            }
            for row in rows
        ]
        return jsonify(teams)
    except Exception as e:
        return jsonify({"error": f"Could not fetch team data: {str(e)}"}),
    finally:
        curs.close()
        connection.close()



@app.route('/teams/<int:teamId>', methods=['DELETE'])
def deleteteam(teamId):
    connection = getconnection()

    if not connection:
        return jsonify({"error": "Could not connect to database"})
    try:
        curs = connection.cursor()
        curs.execute("DELETE FROM \"Teams\" WHERE id = %s;", (teamId,))
        connection.commit()
        if curs.rowcount == 0:
            return jsonify({"error": "Team was not found"})
        return 'Complete'
    except Exception as e:
        return jsonify({"error": f"Could not delete team: {str(e)}"})
    finally:
        curs.close()
        connection.close()



@app.route('/teams/<int:teamId>', methods=['PUT'])
def updateteam(teamId):
    connection = getconnection()
    if not connection:
        return jsonify({"error": "Could not connect to database"})

    data = request.get_json()
    name = data.get('name')
    teamcategory = data.get('teamcategory')
    totalscore = data.get('totalscore')
    scores = data.get('scores')

    try:
        curs = connection.cursor()
        curs.execute("""
            UPDATE "Teams" SET name = %s, teamcategory = %s, totalscore = %s, scores = %s WHERE id = %s""", 
            (name, teamcategory, totalscore, scores, teamId))
        connection.commit()
        if curs.rowcount == 0:
            return jsonify({"error": "Team not found"})
        return jsonify()
    except Exception as e:
        return jsonify({"error": f"Could not update team: {str(e)}"})
    finally:
        curs.close()
        connection.close()

if __name__ == '__main__':
    app.run(debug=True, port=5000)