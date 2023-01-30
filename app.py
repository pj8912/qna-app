from flask import Flask, render_template, redirect, request, session
import mysql.connector
import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
import urllib.parse



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


#login
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        uname  = request.form['uname']
        pwd = request.form['pwd']
        # cursor.execute("SELECT user_pwd FROM users WHERE user_uname = %s",(uname,))
        cursor.execute("SELECT * FROM users WHERE user_uname = %s",(uname,))  
        result = cursor.fetchone()
        if result and check_password_hash(result[3], pwd):
            #set session
            session['username'] = uname
            session['u_id'] = result[0]
            return redirect('/')
        else:
            return redirect('/register')

    return render_template('/')


#logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

@app.route('/about')
def about():
    if 'username' in session:
        return render_template('about.html', appname=APP_NAME, logged_in=True, uname=session['username'])
    else:
        return render_template('about.html', appname=APP_NAME, logged_in=False)


#home
@app.route('/')
def home():
    if 'username' in session:
        cursor.execute("SELECT * FROM questions")  
        result = cursor.fetchall()
        return render_template('index.html', logged_in=True, questions=result, uname=session['username'])
    else:
        return render_template('index.html', logged_in=False, appname=APP_NAME)



#signup form
@app.route('/register')
def register():
     if 'username' in session:
        return redirect('/')
     else:
        return render_template('signup.html', appname=APP_NAME)


#ask
@app.route('/ask')
def ask():   
    if 'username' in session:
        return render_template('ask.html', logged_in=True, uname=session['username'])
    else:
        return redirect('/')

#upload question
@app.route('/uploadq', methods=['POST'])
def upload_question():
    if 'username' in session:
        if request.method == 'POST':
            question  = request.form['question']
            userid = session['u_id']
            cursor.execute("INSERT INTO questions(question,user_id) VALUES(%s, %s)", (question, userid))
            cnx.commit()
            return redirect('/')
    else:
        return redirect('/')        


#profile
@app.route('/profile')
def profile():
    if 'username' in session:
        cursor.execute("SELECT * FROM questions WHERE user_id = %s ", (session['u_id'], ))  
        result = cursor.fetchall()
        cursor.execute("SELECT * FROM answers WHERE user_id= %s", (session['u_id'], ))
        answers = cursor.fetchall()
        return render_template('profile.html', uname=session['username'], logged_in=True, questions=result, answers=answers)
    else:
        return redirect('/')


#view question and related answers
@app.route('/question/<int:id>/<string:qu>')
def question(id, qu):
    if 'username' in session:
        qu = qu.replace("-", " ")
        cursor.execute("SELECT * FROM answers WHERE q_id=%s", (id,))
        answers = cursor.fetchall()
        return render_template('question.html', question=qu, qid=id ,answers=answers ,uname=session['username'], logged_in=True)
    else:
        return redirect('/')

#add answer page
@app.route('/add-answer/<int:q_id>/<string:question>')
def add_answer(q_id, question):
    if 'username' in session:
        question = question.replace("-", " ")
        return render_template('answer.html', qid=q_id , question=question, logged_in=True)
    else:
        return redirect('/')
    


#upload answer
@app.route('/upload-answer', methods=['POST'])
def upload_answer():
    if 'username' in session:
        answer = request.form['answer']
        qid = request.form['qid']
        question  = request.form['question']
        cursor.execute("INSERT INTO answers(q_id, answer, user_id) VALUES(%s, %s, %s)", (qid,answer,session['u_id'] ))
        cnx.commit()
        q = question.replace(" ", "-")
        q = urllib.parse.unquote(q)
        q = urllib.parse.quote(q)
        return redirect(f'/question/{qid}/{q}')
    else:
        return redirect('/')


#delete answer
@app.route('/answer/delete/<int:aid>')
def delete_answer(aid):
    if 'username' in session:
        cursor.execute("DELETE FROM answers WHERE aid=%s", (aid,))
        return redirect('/profile')
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)