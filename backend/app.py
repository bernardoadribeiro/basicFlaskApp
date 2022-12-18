from flask import Flask, render_template
from decouple import config

app = Flask(__name__)

#  used to encrypt and secure your cookies and section data related to web app
app.config['SECRET_KEY'] = config('SECRET_KEY')


@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        host='localhost',
        port=8000,
        use_reloader=True,
        debug=True,
    )
