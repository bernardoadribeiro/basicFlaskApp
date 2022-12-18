from flask import Flask, render_template
from decouple import config

app = Flask(__name__)

# #  set the patch to templates and static
# app.template_folder = './backend/templates/'
# app.static_folder = './backend/static/'


@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        host='localhost',
        port=config('FLASK_RUN_PORT'),
        use_reloader=True,
        debug=config('FLASK_DEBUG'),
    )
