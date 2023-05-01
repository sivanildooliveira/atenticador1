from MyApp import app, db
from flask import render_template, url_for, redirect
from datetime import datetime


@app.route('/')
def home():
    eventos = db.collection('teste').stream()
    return render_template('home.html')

@app.route('/verificar/<numero>')
def verificar(numero):
    lista = db.collection('teste').stream()
    list = []
    result = True
    for i, iten in enumerate(lista):
        
        try:
            nun = iten.to_dict()
            list.append((nun['numero'], nun['hora']))
            if str(numero) == str(nun['numero']):
                result = False
        except:
            pass

    if result and numero != 'j':
        data = {'numero': numero, 'hora': str(datetime.now().strftime('%H:%M:%S'))}
        list.append((numero, data['hora']))
        db.collection('teste').document(numero).set(data)

    return {'lista': list, 'result': result}
