from flask import render_template, request, Blueprint
app = Blueprint('app', __name__)

@app.route("/")
def app_home():
	return render_template('app/home.html')
