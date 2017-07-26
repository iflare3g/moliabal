from flask import request,render_template,url_for,redirect,session,flash
from app.models.login import *


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
            print 'Invalid credentials!'
            return redirect(url_for('area'))
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