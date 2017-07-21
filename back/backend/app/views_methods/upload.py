from flask import request,render_template,url_for,redirect,abort
from app import photos
import flask_uploads
from app.config.config import dest_folder,get_dest_folder

def upload():
    if request.method == 'POST': 
        try:
            if 'catalogo' in request.files:
                
                title = request.form.get('prodotto')
                file = request.files.get('catalogo',None)
                try:
                    filename = photos.save(file,folder='catalogo')
                    return title + ' ' + filename
                except:
                    return 'error'
                
                
            elif 'showroom' in request.files:
    
                filename = photos.save(request.files.get('showroom',None),folder='showroom')
                return  filename
                
        except flask_uploads.UploadNotAllowed as err:
            return 'Your file is not allowed. Please upload only images.' + str(err)
    else:
        return redirect(url_for('prodotto'))
    return redirect(url_for('prodotto'))

