import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Anomaly Detection for Dynamic Graphs</h1>'

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))