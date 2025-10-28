from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# ---------- Database setup ----------
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    department TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

init_db()

# ---------- Home Route ----------
@app.route('/')
def index():
    return render_template('index.html')

# ---------- Insert Data ----------
@app.route('/add', methods=['POST'])
def add_employee():
    name = request.form['name']
    email = request.form['email']
    department = request.form['department']

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO employees (name, email, department) VALUES (?, ?, ?)",
              (name, email, department))
    conn.commit()
    conn.close()
    return redirect('/view')

# ---------- View Data ----------
@app.route('/view')
def view_employees():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM employees")
    data = c.fetchall()
    conn.close()
    return render_template('view.html', employees=data)

if __name__ == '__main__':
    app.run(debug=True)
