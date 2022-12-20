from flask import Blueprint, render_template, request, flash
from werkzeug.security import generate_password_hash, check_password_hash


user = Blueprint(
        'user', __name__,
        template_folder='templates'
    )


@user.route('/user', methods=['GET', 'POST'])
def index():
    """Returns 'user' index page"""

    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Check if information provided is valid
        if len(name) < 3:
            flash('Name must be greater than 2 characters.', category='error')
        elif len(username) < 3:
            flash('Username must be greater than 2 characters.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            from ..models.User import User, db

            new_user = User(name=name, username=username, email=email,
                password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()

            flash('User created!', category='success')

    return render_template('./user/index.html')
