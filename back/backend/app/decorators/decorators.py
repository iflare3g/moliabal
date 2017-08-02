from functools import wraps
from flask import session,redirect,url_for,abort
from app.config.config import EMAIL

def login_required(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if not session and 'username' not in session:
            return redirect(url_for('area'))
        return f(*args,**kwargs)
    return decorated_function
    
def admin_required(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if session and 'username' in session:
            if not session.get('username',None) == EMAIL.get('mail',None):
                abort(404)
        return f(*args,**kwargs)
    return decorated_function