from flask import Flask, render_template, request, redirect, url_for, session, \
    flash, g, Blueprint
from form import LoginForm, RegisterForm
from mybank.models import User, bcrypt
from flask.ext.login import login_user, logout_user, login_required
from mybank import db


users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)

@users_blueprint.route('/login', methods=['GET','POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user=User.query.filter_by(name=request.form['username']).first()
            if user is not None and bcrypt.check_password_hash(user.password, request.form['username']):
                login_user(user)
                flash('you are logged in')
                #return redirect(url_for('home.home'))
                return "Welcome to my bank"
            else:
                error = 'Invalied credentials, Please try again'
    return render_template('login.html', form=form, error=error)
    #return "hello"

@users_blueprint.route('/logout')
def logout():
    logout_user()
    flash('You were just logged out')
    return redirect(url_for('home.welcome'))

if __name__=='__main__':
    users_blueprint.run(debug=True)

