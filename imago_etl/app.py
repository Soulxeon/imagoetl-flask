from flask import Flask, render_template, request
from db_imago.connect import connect
from csv_imago.read_df import read_data

app = Flask(__name__)
# app.static_folder = 'static'

@app.route('/')
def index():
    db_data = connect()
    return render_template('index.html', testdata=db_data)

@app.route('/csv', methods=['GET','POST'])
def csv_index():
    return render_template('csvform.html')

@app.route('/data', methods=['GET','POST'])
def data():
    if request.method == 'POST':
        f = request.files["csvdata"]
        data = read_data(f)
        return render_template('table.html', tables=[data.to_html()], titles=[''])

app.run(host="0.0.0.0", port=5000, debug=True)