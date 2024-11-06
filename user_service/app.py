from quart import Quart, request, jsonify
import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Quart(__name__)

DATABASE_URL = os.getenv('DATABASE_URL')  # Get DATABASE_URL from .env

async def connect_to_db():
    try:
        connection = await asyncpg.connect(DATABASE_URL)
        print("Connected to the database")
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        raise

@app.before_serving
async def startup():
    # Connect to DB and create table before serving requests
    app.db = await connect_to_db()
    await create_table()  # Ensure table is created before serving requests

@app.after_serving
async def shutdown():
    # Close the database connection after serving requests
    await app.db.close()

# Create the users table if it doesn't exist
async def create_table():
    try:
        await app.db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(80) UNIQUE NOT NULL,
                password VARCHAR(120) NOT NULL
            )
        ''')
        print("Table created or already exists")
    except Exception as e:
        print(f"Error creating table: {e}")

# User registration endpoint
@app.route('/register', methods=['POST'])
async def register():
    data = await request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400

    query = 'INSERT INTO users(username, password) VALUES($1, $2)'
    try:
        await app.db.execute(query, username, password)
        return jsonify({"message": "User registered successfully!"}), 201
    except asyncpg.UniqueViolationError:
        return jsonify({"error": "Username already exists."}), 400
    except Exception as e:
        print(f"Error during registration: {e}")
        return jsonify({"error": "Internal server error."}), 500

# User login endpoint
@app.route('/login', methods=['POST'])
async def login():
    data = await request.json
    username = data.get('username')
    password = data.get('password')

    try:
        user = await app.db.fetchrow('SELECT * FROM users WHERE username = $1 AND password = $2', username, password)

        if user:
            return jsonify({"message": "Login successful!"}), 200
        else:
            return jsonify({"error": "Invalid username or password."}), 401
    except Exception as e:
        print(f"Error during login: {e}")
        return jsonify({"error": "Internal server error."}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
