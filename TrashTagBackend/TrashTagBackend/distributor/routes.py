from flask import render_template, request, Blueprint, session, redirect, url_for, flash, jsonify
from TrashTagBackend.distributor.forms import *
from TrashTagBackend.models import *
from TrashTagBackend import db, qr

distributor = Blueprint('distributor', __name__)

@distributor.route("/",methods=['GET', 'POST'])
def home():
	if(not session.get('d_uname') or not session.get('d_pass')):
		flash('Please Login to Access', 'info')
		return redirect(url_for('distributor.login', next='distributor.home'))

	dist = DistributorModel.query.filter_by(username=session['d_uname']).first()
	
	if(request.method=='POST'):
		data = request.form
		loc = LocationModel(f"Dustbin<{data['dname']}>", data['lat'], data['lng'])

		if(LocationModel.query.filter_by(lat=data['lat'], lng=data['lng']).first()):
			loc = LocationModel.query.filter_by(lat=data['lat'], lng=data['lng']).first()

		d = Dustbin(
			name=data['dname'],
			dustbin_type=data['dtype'],
			location=loc,
			distributor=dist
		)
		db.session.add(d)
		db.session.commit()
		return jsonify({'qrkey':d.dustbinkey})
	return render_template('distributor/dhome.html', title="distributor")

@distributor.route("/login", methods=['GET', 'POST'])
def login():
	form = DistributorLoginForm()
	if(form.validate_on_submit()):
		uname, pwd = form.username.data, form.password.data
		p = DistributorModel.query.filter_by(username=uname).first()

		if(not p):
			flash('Invalid Credentials', 'danger')
			return render_template('distributor/dlogin.html', title='Distributor Login', form=form)

		if(p.password == pwd):
			nxt = request.args.get('next')
			session['d_uname'] = p.username
			session['d_pass'] = p.password
			if(nxt): return redirect(url_for(nxt))
			
			return redirect(url_for('distributor.home'))
		else:
			flash('Invalid Credentials', 'danger')
			return render_template('distributor/dlogin.html', title='Distributor Login', form=form)

	return render_template('distributor/dlogin.html', title="Distributor Login", form=form)

@distributor.route('/register', methods=['GET', 'POST'])
def register():
	form = DistributorRegisterForm()
	if(form.validate_on_submit()):
		name, uname, pwd = form.name.data, form.username.data, form.password.data
		p = DistributorModel(
			name=name,
			uname=uname,
			pwd=pwd,
		)
		db.session.add(p)
		db.session.commit()
		flash('Login to Continue', 'info')
		return redirect(url_for('distributor.login'))
	return render_template('distributor/dreg.html', title="distributor Register", form=form)

@distributor.route('/logout')
def logout():
	session['d_uname'] = None
	session['d_pass'] = None
	return redirect(url_for('distributor.login'))
	

@distributor.route('/qrviewer/<qkey>')
def qrviewer(qkey):
	return render_template('distributor/qr.html', qr=qr.qrcode(qkey))