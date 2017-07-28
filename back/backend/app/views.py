from flask import Flask,jsonify,render_template,url_for,request,session,redirect
from app import app
from views_methods.upload import *
from views_methods.login import *
from views_methods.get_folder import *
from decorators.decorators import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')
    
@app.route('/galleria')
def galleria():
    return render_template('galleria.html')
    
@app.route('/location')
def location():
    return render_template('location.html')
    
@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/contact')
def contacts():
    return render_template('contact.html')

    
@app.route('/about')
def about():
    return render_template('about.html')
    
@app.route('/prodotto')
@login_required
@admin_required
def prodotto():
    return render_template('amministra.html')
    
@app.route('/catalogo')
@login_required
def catalogo():
    return render_template('riservato.html')
    
@app.route('/upload',methods=['GET','POST'])
@login_required
def carica():
   return upload()
    
@app.route('/area',methods=['GET','POST'])
def area():
    return valid_login()
    
@app.route('/logout',methods=['GET'])
def logout_area():
    return logout()
    
@app.route('/getFolder',methods=['GET'])
@login_required
@admin_required
def get_fold():
    return get_folder()
    
@app.route('/deleteFile',methods=['GET'])
@login_required
@admin_required
def delete():
    return remove('app/static/img/showroom/super.jpg')
    
@app.errorhandler(413)
def file_not_allowed(e):
    return "Non puoi caricare un file di dimensioni maggiori a 16 MB. ERRORE HTTP/1.1 413", 413  
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404page.html')