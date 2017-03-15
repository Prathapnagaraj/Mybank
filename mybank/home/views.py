from mybank import app, db
#from mybank.models import
#from form import AcountForm
from flask import render_template, request, url_for, \
    session, flash, Blueprint
#from flask.ext.login import login_required, current_user
from flask_login import login_required, current_user

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)


@home_blueprint.route('/my_bank')
def home():
    #return "hello"
    return render_template("first_page.html")





