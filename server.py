from flask import Flask
import numpy as np
import joblib
from tensorflow.keras.models import load_model

app = Flask(__name__)

reg = joblib.load("models/regression.pkl")
print(speed = myfunc(w))

model = load_model("models/neural.h5")


@app.route('/')
def index():
    return app.send_static_file('index.html')

# Regression
@app.route('/api/model1/<int:w>')
def model1(w):
    p = list(map(speed, [[w]]))
    return {"value": str(p[0])} 

# Neural  
@app.route('/api/model2/<int:w>')
def model2(w):
    p = model.predict([[w]]) 
    return {"value": str(p[0][0])}


if __name__ == "__main__":
    app.run(debug = True)