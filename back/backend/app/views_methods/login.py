from flask import request,render_template,url_for,redirect,session,flash
from functools import wraps
from app.models.login import *

def login_required(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if not session and 'username' not in session:
            return redirect(url_for('area'))
        return f(*args,**kwargs)
    return decorated_function
    
def valid_login():
    res = None
    if request.method == 'POST':
        email = request.form.get('email',None)
        pwd = request.form.get('password',None)
        res = login(email,pwd)
        if res:
            session['username'] = email
            return redirect(url_for('catalogo'))
        else:
            flash('Invalid credentials!')
            return redirect(url_for('area'))
    else:
        return render_template('area.html')
            
            