from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Create a SQLite database and connect to it
conn = sqlite3.connect('coffeeteria.db', check_same_thread=False)
cursor = conn.cursor()

# Create a table for user registration
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')
conn.commit()

@app.route('/')
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Check if the user exists in the database
        cursor.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
        user = cursor.fetchone()
        
        if user:
            # Redirect to the home page after successful login
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid email or password')
    else:
        # Render the login page
        return render_template('login.html')


@app.route('/register', methods=['POST'])
def register_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Insert the user data into the database
        cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
        conn.commit()
        
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    # Perform logout actions here if necessary
    return redirect(url_for('register'))  # Redirect to the register page after logout

if __name__ == '__main__':
    app.run(debug=True)
