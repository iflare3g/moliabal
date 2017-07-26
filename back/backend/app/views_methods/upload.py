from flask import request,render_template,url_for,redirect,abort
from app import docs,photos
import flask_uploads
from app.config.config import SUBFOLDERS

def upload():
    if request.method == 'POST': 
            if 'catalogo' in request.files:
                print request.files
                title = request.form.get('prodotto')
                file = request.files.get('catalogo',None)
                try:
                    filename = docs.save(file)
                    return title + ' ' + filename
                except flask_uploads.UploadNotAllowed:
                    abort(500)
                
            elif 'showroom' in request.files:
                print request.files
                try:
                    filename = photos.save(request.files.get('showroom',None))
                    return  filename
                except flask_uploads.UploadNotAllowed:
                    abort(500)
    else:
        return redirect(url_for('prodotto'))
    return redirect(url_for('prodotto'))

