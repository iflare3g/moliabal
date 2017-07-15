from flask import request,render_template,url_for,redirect
from app import photos
import flask_uploads

def upload():
    if request.method == 'POST' and 'img' in request.files:
        try:
            filename = photos.save(request.files['img'])
            title = request.form.get('prodotto')
            return title + ' ' + filename 
        except flask_uploads.UploadNotAllowed as err:
            return 'Your file is not allowed. Please upload only images.' + str(err)
    else:
        return redirect(url_for('prodotto'))
    return redirect(url_for('prodotto'))
''