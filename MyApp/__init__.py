from flask import Flask
import firebase_admin
from firebase_admin import firestore, credentials

app = Flask(__name__)


cred = credentials.Certificate('MyApp/keys/key.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


from MyApp import routes