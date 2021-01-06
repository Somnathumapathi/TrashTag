from flask import render_template, request, Blueprint
producer = Blueprint('producer', __name__)

@producer.route("/")
def producer_home():
	return render_template('phome.html', title="Distributor")
