from flask import request,render_template,url_for,redirect,session
from app.models.login import *
from app.config.config import EMAIL


def valid_login():
    res = None
    error = ""
    if request.method == 'POST':
        email = request.form.get('email',None)
        pwd = request.form.get('password',None)
        if email is not None and pwd is not None:
            res,param = login(email,pwd)
        if res:
            session['username'] = email
            return redirect(url_for('catalogo',param=param))
        else:
            error = 'Invalid credentials!'
            return render_template('area.html',error=error)
    elif request.method == 'GET' and 'username' in session:
        return redirect(url_for('catalogo'))
    else:
        return render_template('area.html')
    
            
def logout():
    if session and 'username' in session:
        session.pop('username',None)
    else:
        return redirect(url_for('area'))
    return redirect(url_for('area'))