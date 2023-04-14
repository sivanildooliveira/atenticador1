from MyApp import app, db
from flask import render_template, url_for, redirect
from datetime import datetime


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/verificar/<numero>')
def verificar(numero):
    lista = db.collection('lista').stream()
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

    if result:
        data = {'numero': numero, 'hora': str(datetime.now().strftime('%H:%M:%S'))}
        list.append((numero, data['hora']))
        db.collection('lista').document(numero).set(data)

    return {'lista': list, 'result': result}
