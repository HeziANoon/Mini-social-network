from app.models import User, engine
from flask import render_template, request, session, redirect
from sqlalchemy.orm import Session

from . import app

@app.route('/')
def page():
    return "Mini Social Network"

#Page with news
@app.route('/feed')
def feed():
    return render_template('feed.html')

#Page Login
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        with Session(engine) as db_session:
            user = db_session.query(User).filter_by(email=email).first()
            if user:
                if user.check_password(password):
                    session['user_id'] = user.id
                    return redirect('/feed')
                else:
                    return "Wrong password, retry. <a href='/login'>Retry</a>"
            else:
                return "User was not found. <a href='/register'>Register</a>"
    else:
        return render_template('login.html')
    
#Page Register
@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        
        with Session(engine) as db_session:
            user = User(
                username=username,
                email=email
            )
            user.set_password(password)
            db_session.add(user)
            db_session.commit()
            return "Registration is successfully! <a href='/login'>Login</a>"
    else:
        return render_template('register.html')
    

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/login')