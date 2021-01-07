from flask import render_template, request, Blueprint, jsonify
from TrashTagBackend import db
from TrashTagBackend.models import *
api = Blueprint('api', __name__)

@api.route("/")
def main_home():
	return render_template('home.html', title='TrashTag')

#=============================================USERS=====================================================
@api.route('/loginuser/<username>/<password>')
def login_user(username, password):

	U = UserModel.query.filter_by(username=username).first()
	if(not U): return jsonify({'status': 0, 'message': 'User not Found'})
	if(password == U.password):
		return jsonify({'status': 200, 'message': 'OK', 'username':U.username})

	return jsonify({'status': 0, 'message': 'Incorrect Credentials'})

@api.route('/registeruser/<name>/<username>/<password>')
def register_user(name, username, password):

	U = UserModel(uname=username, pwd=password, name=name)
	db.session.add(U)
	db.session.commit()

	return jsonify({'status': 200, 'message': 'OK'})
#============================================/USERS=====================================================


@api.route("/getdustbins")
def get_dustbins():
	dbs = Dustbin.query.all()
	return jsonify({
		'status': 200,
		'message':'OK',
		'dustbins': [
			{
				'name': x.name,
				'latitude': x.location.lat,
				'longitude': x.location.lng,
			} for x in dbs
		]
	})

@api.route("/add2dustbin/<uname>/<productkey>/<dustbinkey>")
def addproduct2dubstin(uname, productkey, dustbinkey):
	user = UserModel.query.filter_by(username=uname).first()
	product = Product.query.filter_by(productkey=productkey).first()
	dustbin = Dustbin.query.filter_by(dustbinkey=dustbinkey).first()
	print(f"USERRRRR  ---> {user}")
	if(not user or not product or not dustbin): return jsonify({'status':0, 'message':'Incorrect Information'})
	print(f"{user} : Adding {product} --> {dustbin}")
	product.add2dustbin(user, dustbin)
	return jsonify({
		'status': 200,
		'message': 'OK',
		'coins': int(user.coins)
	})
