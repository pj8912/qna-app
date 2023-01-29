from flask import Flask, render_template, redirect, request, session
import mysql.connector
import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash


load_dotenv()
app = Flask(__name__) #Flask app
app.secret_key = 'YOUR_SECRET_KEY'
#DB config
HOST = os.environ.get("DB_HOST")
USERNAME = os.environ.get("DB_USERNAME")
PWD = os.environ.get("DB_PWD")
DBNAME = os.environ.get("DB_NAME")

APP_NAME = os.environ.get("APP_NAME")




#mysqlconnection
cnx = mysql.connector.connect(user=USERNAME, password=PWD, host=HOST, database=DBNAME)
cursor = cnx.cursor()



#register user
@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        
        flname = request.form['flname']
        uname = request.form['uname']
        pwd = request.form['pwd']
        
        #check if user already exists
        cursor.execute("SELECT * FROM users WHERE user_uname = %s", (uname,))
        result = cursor.fetchone()
        if result:
            return redirect('/register')
        else:
            hashed_pwd = generate_password_hash(pwd, method='sha256')
            cursor.execute("INSERT INTO users(fullname, user_uname, user_pwd) VALUES(%s, %s, %s)", (flname, uname, hashed_pwd))
            cnx.commit()
            return redirect('/')

    return render_template('signup.html')



@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        uname  = request.form['uname']
        pwd = request.form['pwd']
        cursor.execute("SELECT user_pwd FROM users WHERE user_uname = %s",(uname,))
        result = cursor.fetchone()
        if result and check_password_hash(result[0], pwd):
            #set session
            session['username'] = uname
            return redirect('/')
        else:
            return redirect('/register')

    return render_template('/')


#logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')



#home
@app.route('/')
def home():
    if 'username' in session:
        return render_template('index.html', logged_in=True)
    else:
        return render_template('index.html', logged_in=False, app_name=APP_NAME)



#signup form
@app.route('/register')
def register():
     if 'username' in session:
        return redirect('/')
     else:
        return render_template('signup.html', appname=APP_NAME)





if __name__ == '__main__':
    app.run(debug=True)