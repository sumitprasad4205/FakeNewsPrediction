from flask import Flask,render_template,request
import joblib
import pandas as pd
model = joblib.load('news.pkl')

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def predict():
    if request.method =='POST':
        text = request.form['text']

        text = pd.Series('text')
        prediction = model.predict(text)

        return render_template('index.html',prediction=f'{prediction[0].capitalize()} News')

    return render_template('index.html')

app.run(debug=True)