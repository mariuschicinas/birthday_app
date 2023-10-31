from flask import Flask, request, jsonify
import mysql.connector
from datetime import date
import os
import time
import logging


app = Flask(__name__)

# Function to create a MySQL database connection with retry logic
def create_database_connection():
    while True:
        try:
            connection = mysql.connector.connect(
                host=os.environ.get("MYSQL_HOST"),
                user=os.environ.get("MYSQL_USER"),
                password=os.environ.get("MYSQL_PASSWORD"),
                database=os.environ.get("MYSQL_DB"),
            )
            if connection.is_connected():
                return connection
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            print("Retrying database connection in 5 seconds...")
            time.sleep(5)

# Function to create the 'users' table if it doesn't exist
def create_users_table():
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) UNIQUE,
                date_of_birth DATE
            )
        ''')
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error creating 'users' table: {err}")

# Usage:
conn = create_database_connection()
create_users_table()

@app.route('/hello/<username>', methods=['PUT'])
def put_birthday(username):
    # Ensure username contains only letters
    if not username.isalpha():
        return "Username must contain only letters", 400

    data = request.get_json()
    date_of_birth = data.get('dateOfBirth')

    # Validate date_of_birth format and check if it's before today
    try:
        dob = date.fromisoformat(date_of_birth)
        today = date.today()
        if dob >= today:
            return "Invalid dateOfBirth", 400
    except ValueError:
        return "Invalid dateOfBirth format (YYYY-MM-DD)", 400

    # Insert or update user data into the database
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, date_of_birth) VALUES (%s, %s) ON DUPLICATE KEY UPDATE date_of_birth = VALUES(date_of_birth)", (username, date_of_birth))
        conn.commit()
    except mysql.connector.Error as err:
        return f"Database error: {err}", 500

    return '', 204


@app.route('/hello/<username>', methods=['GET'])
def get_birthday(username):
    print(f"Received GET request for username: {username}")

    # Retrieve user data from the database
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT date_of_birth FROM users WHERE username=%s", (username,))
        row = cursor.fetchone()

        app.logger.debug(f"Received request for username: {username}: {row}")


        if row is not None:
            dob = row[0]
            if True:
                try:
                    today = date.today()
                    next_birthday = date(today.year,dob.month,dob.day)
                    days_until_birthday = (next_birthday - today).days
                    if days_until_birthday < 0:
                        next_birthday = date(today.year+1,dob.month,dob.day)
                        days_until_birthday = (next_birthday - today).days
                    if days_until_birthday == 0:
                        return jsonify({"message": f"Hello, {username}! Happy birthday!"})
                    elif days_until_birthday > 0:
                        return jsonify({"message": f"Hello, {username}! Your birthday is in {days_until_birthday} day(s)"})
                except ValueError as e:
                    return f"Invalid date_of_birth format: {e}", 400
        else:
            return "User not found 1", 404

    except mysql.connector.Error as err:
        return f"Database error: {err}", 500

    return "User not found 2", 404



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
