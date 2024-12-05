from flask import Flask, jsonify, request
from database import get_db_connection

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Postgres Dockerized App!"})


@app.route('/add', methods=['POST'])
def add_record():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO records (name, age) VALUES (%s, %s) RETURNING id;",
        (data['name'], data['age'])
    )
    record_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"id": record_id, "message": "Record added!"}), 201


@app.route('/records', methods=['GET'])
def get_records():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM records;")
    records = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(records)


# Run condition for Flask-server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
