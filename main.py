from flask import Flask, render_template, url_for

app = Flask('app')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/answeris5')
def answeris5():
    return render_template('answeris5/index.html')
app.run(host='127.0.0.1', port=5500)