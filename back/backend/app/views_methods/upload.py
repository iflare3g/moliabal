from flask import request,render_template,url_for,redirect,abort
from app import docs,photos
import flask_uploads
from app.config.config import SUBFOLDERS

def upload():
    if request.method == 'POST': 
            if 'catalogo' in request.files:
                print request.files
                file = request.files.get('catalogo',None)
                try:
                    filename = docs.save(file)
                    return filename
                except flask_uploads.UploadNotAllowed:
                    abort(500)
                
            elif 'img' in request.files:
                print request.files
                sub_folder = request.form.get('choose',None).lower().replace(' ','')
                print sub_folder
                try:
                    filename = photos.save(request.files.get('img',None),folder=sub_folder)
                    return  filename
                except flask_uploads.UploadNotAllowed:
                    abort(500)
    else:
        return redirect(url_for('prodotto'))
    return redirect(url_for('prodotto'))

