from flask import Flask
import random

app = Flask(__name__)

@app.route('/api/getRandom')
def getRandom():
    return str(random.randint(0, 100))
