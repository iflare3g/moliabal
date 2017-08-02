from flask import render_template,request
from app.config.config import EMAIL

def riservato():
    email = EMAIL.get('mail',None)
    param = request.args.get('param',None)
    if param is not None:
        return render_template('riservato.html',parameter=param,email=email)
    else:
        return render_template('riservato.html',email=email)
