from flask import Flask, render_template_string, request, redirect, url_for, session
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Secret key for session management
app.secret_key = 'your_secret_key'

# Path to save uploaded images
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Hardcoded password for admin panel
ADMIN_PASSWORD = 'TH3_FAIZU'

# In-memory user data (replace with a database in production)
users = []

# HTML Templates embedded in Python
login_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            padding: 50px;
            text-align: center;
        }
        input {
            padding: 10px;
            margin: 10px;
            width: 200px;
        }
        .btn {
            padding: 10px 20px;
            background-color: #5cb85c;
            color: white;
            border: none;
            cursor: pointer;
        }
        .btn:hover {
            background-color: #4cae4c;
        }
    </style>
</head>
<body>
    <h1>Login</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="text" name="username" placeholder="Enter Username" required><br>
        <input type="password" name="password" placeholder="Enter Password" required><br>
        <input type="file" name="image"><br><br>
        <button type="submit" class="btn">Login</button>
    </form>
</body>
</html>
"""

visit_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visit</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
            background-image: url('https://raw.githubusercontent.com/FaiziXd/Lun-dhek-le-aja/refs/heads/main/e26997b607ccc1c89c4946c789e0c227.jpg');
            background-size: cover;
        }
        .btn {
            padding: 10px 20px;
            background-color: #5cb85c;
            color: white;
            border: none;
            cursor: pointer;
        }
        .btn:hover {
            background-color: #4cae4c;
        }
        .profile-img {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <h1>Welcome {{ username }}!</h1>
    {% if image %}
        <img src="{{ url_for('static', filename='uploads/' + image) }}" class="profile-img" alt="Profile Picture">
    {% endif %}
    <br><br>
    <a href="https://faizuhere.onrender.com/" class="btn">Visit</a>
</body>
</html>
"""

admin_login_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Panel</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            padding: 50px;
            text-align: center;
        }
        .btn {
            padding: 10px 20px;
            background-color: #5cb85c;
            color: white;
            border: none;
            cursor: pointer;
        }
        .btn:hover {
            background-color: #4cae4c;
        }
        table {
            width: 100%;
            margin-top: 20px;
            border-collapse: collapse;
        }
        table, th, td {
            border: 1px solid black;
        }
        th, td {
            padding: 10px;
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>Admin Panel</h1>
    <form method="POST">
        <input type="password" name="admin_password" placeholder="Enter Admin Password" required><br><br>
        <button type="submit" class="btn">Login to Admin</button>
    </form>
</body>
</html>
"""

admin_panel_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Panel</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            padding: 50px;
            text-align: center;
        }
        .btn {
            padding: 10px 20px;
            background-color: #5cb85c;
            color: white;
            border: none;
            cursor: pointer;
        }
        .btn:hover {
            background-color: #4cae4c;
        }
        table {
            width: 100%;
            margin-top: 20px;
            border-collapse: collapse;
        }
        table, th, td {
            border: 1px solid black;
        }
        th, td {
            padding: 10px;
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>Admin Panel - Manage Users</h1>
    <table>
        <tr>
            <th>Username</th>
            <th>Profile Image</th>
            <th>Action</th>
        </tr>
        {% for user in users %}
        <tr>
            <td>{{ user['username'] }}</td>
            <td>
                <img src="{{ url_for('static', filename='uploads/' + user['image']) }}" width="50" height="50">
            </td>
            <td>
                <form method="POST" action="{{ url_for('delete_user', username=user['username']) }}">
                    <button type="submit" class="btn">Delete</button>
                </form>
            </td>
        </tr>
        {% endfor %}
    </table>
    <br>
    <a href="{{ url_for('admin') }}" class="btn">Back to Admin Login</a>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        image = request.files.get('image')

        # Save image if provided
        if image:
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image_path = filename
        else:
            image_path = None
        
        # Store user data in session
        session['username'] = username
        session['image'] = image_path
        
        # Redirect to visit page
        return redirect(url_for('visit'))
    
    return render_template_string(login_html)

@app.route('/visit')
def visit():
    if 'username' in session:
        return render_template_string(visit_html, username=session['username'], image=session.get('image'))
    return redirect(url_for('login'))

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        admin_password = request.form['admin_password']
        if admin_password == ADMIN_PASSWORD:
            return render_template_string(admin_panel_html, users=users)
        else:
            return "Invalid Admin Password!"
    return render_template_string(admin_login_html)

@app.route('/delete_user/<username>', methods=['POST'])
def delete_user(username):
    # Remove user from the list
    global users
    users = [user for user in users if user['username'] != username]
    return redirect(url_for('admin'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
