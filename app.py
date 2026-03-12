
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    data = pd.read_csv('data/heart_disease.csv')

    total_patients = len(data)
    heart_patients = int(data['target'].sum())
    male = len(data[data['sex']==1])
    female = len(data[data['sex']==0])
    avg_chol = round(data['chol'].mean(),2)

    stats = {
        "total": total_patients,
        "heart": heart_patients,
        "male": male,
        "female": female,
        "chol": avg_chol
    }

    return render_template("index.html", stats=stats)

if __name__ == '__main__':
    app.run(debug=True)
