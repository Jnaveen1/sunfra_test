from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)


# Create database and table
def create_database():
    conn = sqlite3.connect("mydatabase.db")

    conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
    """)

    conn.commit()
    conn.close()


create_database()


# Display HTML page
@app.route("/")
def home():
    return render_template("page.html")


# Save data into database
@app.route("/save", methods=["POST"])
def save():

    data = request.json

    name = data["name"]
    email = data["email"]

    conn = sqlite3.connect("mydatabase.db")

    conn.execute(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        (name, email)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Data saved successfully"
    })


# View saved data (for testing)
@app.route("/users")
def users():

    conn = sqlite3.connect("mydatabase.db")

    data = conn.execute(
        "SELECT * FROM users"
    ).fetchall()

    conn.close()

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)