from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Route for home page
@app.route('/')
def home():
    # Load data and perform necessary data preprocessing
    df = pd.read_csv('data.csv')

    # Pass data to HTML template for rendering
    return render_template('index.html', data=df.to_html())

if __name__ == '__main__':
    app.run(debug=True)
