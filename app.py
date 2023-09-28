from flask import Flask, render_template, request,redirect
import mysql.connector

app = Flask(__name__)



conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kunal@123",
        database="users"
        )

def close_db_connection():
    if conn:
        conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/sign_in')
def sign_in():
    return render_template('registration.html')

@app.route('/register', methods=['POST'])
def registration():

    uname=request.form.get('uname')
    passwrd=request.form.get('passwrd')
    cursor=conn.cursor()
    cursor.execute("Insert into login_details values(%s,%s)",(uname,passwrd))
    cursor.execute("SELECT * FROM login_details WHERE Name LIKE %s AND Password LIKE %s", (uname, passwrd))
    users = cursor.fetchall()
    if len(users)>0:
        return redirect('/')
    else:    
        conn.commit()
        return redirect('/home')

@app.route('/login_validation', methods=['POST'])
def login_validation():

    username = request.form.get('username')
    password = request.form.get('password')

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM login_details WHERE Name LIKE %s AND Password LIKE %s", (username, password))
    users = cursor.fetchall()
    if len(users)>0:
        return redirect('/home')
    else:    
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
