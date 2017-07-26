from flask import Flask
from flask_uploads import UploadSet,configure_uploads,DOCUMENTS,IMAGES
from flask_cors import CORS
import os
from datetime import timedelta

app = Flask(__name__)
docs = UploadSet('documents',DOCUMENTS)
photos = UploadSet('photos',IMAGES)
app.config['UPLOADED_DOCUMENTS_DEST'] = 'app/static/img/catalogo'
app.config['UPLOADED_PHOTOS_DEST'] = 'app/static/img/showroom'
configure_uploads(app,docs)
configure_uploads(app,photos)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024
CORS(app)
app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(minutes=15)

from app import views

