from flask import Flask, render_template
from db.connect import connect

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

app.run(port=5000)