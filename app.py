from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import sqlite3
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/')
def index():
    return render_template('index.html')


# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Connect to the database
        conn = sqlite3.connect('user_database.db')
        cursor = conn.cursor()

        # Check if the username and password match
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()

        conn.close()

        if user:
            session['username'] = username
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'message': 'Invalid username or password. Please try again.'})

    # Handle GET request to display login page
    return render_template('index.html')  # You can customize this route based on your folder structure

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    error_message = None

    if request.method == 'POST':
        username = request.form['username'].lower()  # Convert username to lowercase
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            error_message = 'Passwords do not match. Please try again.'
            flash(error_message, 'error')
        else:
            # Connect to the database
            conn = sqlite3.connect('user_database.db')
            cursor = conn.cursor()

            # Check if the username already exists (case-insensitive)
            cursor.execute('SELECT * FROM users WHERE lower(username) = ?', (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                error_message = 'Username already exists. Please choose another username.'
                flash(error_message, 'error')
            else:
                # If the username is unique (case-insensitive) and passwords match, insert the new user into the database
                cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
                conn.commit()
                conn.close()

                flash('Registration successful. You can now log in.', 'success')
                return redirect('/login')

    return render_template('registration.html', error_message=error_message)

# Delete user route
@app.route('/delete_user', methods=['POST'])
def delete_user():
    username = request.form['username']

    # Connect to the database
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    # Delete the user from the database
    cursor.execute('DELETE FROM users WHERE username = ?', (username,))
    conn.commit()
    conn.close()

    
    # Redirect to the info page after deleting the user
    return redirect('/info')


# Info route
@app.route('/info')
def info():
    # Connect to the database
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    # Fetch all users
    cursor.execute('SELECT username FROM users')
    users = cursor.fetchall()

    conn.close()

    return render_template('info.html', users=users)

# Dashboard route
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    else:
        return redirect('/login')

# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
