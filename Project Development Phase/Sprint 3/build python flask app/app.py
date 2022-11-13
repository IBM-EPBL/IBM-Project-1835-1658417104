import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

@app.route('/front',methods=['GET','POST'])
@app.route('/')
def home():
    return render_template('/start.html')

@app.route('/end.html')
def end():
    return render_template('/end.html')

@app.route('/index.html')   
def index():
    return render_template('/index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    data=[]
    features = request.form["z1"]
    data.append(features)
    
    model = pickle.load(open('phishing.pkl','rb'))
    result = model.predict(data)
    if result[0]=="bad":
        return render_template('/index.html', prediction_text="This is a phising site")
    else:
        return render_template('/index.html', prediction_text="This is not a phising site")


if __name__ == "__main__":
    app.run(debug=True,use_reloader=False)


from werkzeug.wrappers import Request, Response
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 5000, app)