from flask import render_template,request
from app.config.config import EMAIL

def amministra():
    email=EMAIL.get('mail',None)
    return render_template('amministra.html',email=email)
