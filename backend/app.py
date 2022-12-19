from flask import Flask, render_template
from decouple import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Import routes (to register blueprints)
from .routes import user


app = Flask(__name__)
app.app_context().push()

# #  set the patch to templates and static
# app.template_folder = './backend/templates/'
# app.static_folder = './backend/static/'


#  Setup Database connection
app.config['SQLALCHEMY_DATABASE_URI'] = config('SQLALCHEMY_DATABASE_URI',)
app.config['SQLALCHEMY_ECHO'] = config('SQLALCHEMY_ECHO')

db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db, directory='./backend/migrations')


# Index route
@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')


# Start app
if __name__ == '__main__':
    app.run(
        host='localhost',
        port=config('FLASK_RUN_PORT'),
        use_reloader=True,
        debug=config('FLASK_DEBUG'),
    )

# Register routes
app.register_blueprint(user.user, url_prefix='/')


# Import database models from models
from .models import User