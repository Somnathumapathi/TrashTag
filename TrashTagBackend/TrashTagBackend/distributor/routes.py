from flask import render_template, request, Blueprint
distributor = Blueprint('distributor', __name__)

@distributor.route("/")
def distributor_home():
	return render_template('dhome.html', title="Distributor")

