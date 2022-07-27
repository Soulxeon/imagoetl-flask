from flask import Flask, render_template
from db_imago.connect import connect
from csv_imago.read_df import read_data

app = Flask(__name__)

@app.route('/')
def index():
    conn = connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM test;')
    testdata = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', testdata=testdata)

@app.route('/table')
def table():
    # converting csv to html
    data = read_data()
    return render_template('table.html', tables=[data.to_html()], titles=[''])

app.run(port=5000)