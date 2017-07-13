from flask import Flask,jsonify,render_template,url_for,request,session,redirect
from app import app

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

@app.route('/area')
def area():
    return render_template('area.html')
    
@app.route('/about')
def about():
    return render_template('about.html')
    
@app.route('/prodotto')
def prodotto():
    return render_template('prodotto.html')
    
@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')
    
    