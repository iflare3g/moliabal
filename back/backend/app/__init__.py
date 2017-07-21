from flask import Flask
from flask_uploads import UploadSet,configure_uploads,IMAGES,patch_request_class
from flask_cors import CORS
import os
from datetime import timedelta

app = Flask(__name__)
photos = UploadSet('photos',IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'app/static/img/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
configure_uploads(app,(photos,))
CORS(app)
app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(minutes=15)

from app import views

