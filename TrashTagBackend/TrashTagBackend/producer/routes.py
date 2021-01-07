from flask import render_template, request, Blueprint, session, redirect, url_for, flash, jsonify
from TrashTagBackend.producer.forms import *
from TrashTagBackend.models import *
from TrashTagBackend import db, qr
producer = Blueprint('producer', __name__)

@producer.route("/" ,methods=['GET', 'POST'])
def home():
	if(not session.get('p_uname') or not session.get('p_pass')):
		flash('Please Login to Access Page	', 'info')
		return redirect(url_for('producer.login', next='producer.home'))

	prod = ProducerModel.query.filter_by(username=session['p_uname']).first()
	
	if(request.method=='POST'):
		data = request.form
		p = Product(
			name=data['pname'],
			isbiodegradable= (data['biodegradable'] == 'b'),
			producer=prod,
			waste_type=data['wtype']
		)
		db.session.add(p)
		db.session.commit()
		return jsonify({'qrkey':p.productkey})

	return render_template('producer/phome.html', title="Producer")

@producer.route("/login", methods=['GET', 'POST'])
def login():
	if(session.get('p_pass')): return redirect(url_for('producer.home'))
	form = ProducerLoginForm()
	if(form.validate_on_submit()):
		uname, pwd = form.username.data, form.password.data
		p = ProducerModel.query.filter_by(username=uname).first()

		if(not p):
			flash('Invalid Credentials', 'danger')
			return render_template('producer/plogin.html', title='Producer Login', form=form)

		if(p.password == pwd):
			session['p_uname'] = p.username
			session['p_pass'] = p.password
			nxt = request.args.get('next')
			if(nxt): return redirect(url_for(nxt))
			return redirect(url_for('producer.home'))
		else:
			flash('Invalid Credentials', 'danger')
			return render_template('producer/plogin.html', title='Producer Login', form=form)

	return render_template('producer/plogin.html', title="Producer Login", form=form)

@producer.route('/register', methods=['GET', 'POST'])
def register():
	form = ProducerRegisterForm()
	if(form.validate_on_submit()):
		name, uname, pwd = form.name.data, form.username.data, form.password.data
		p = ProducerModel(
			name=name,
			uname=uname,
			pwd=pwd,
		)
		db.session.add(p)
		db.session.commit()
		flash('Login to Continue', 'info')
		return redirect(url_for('producer.login'))
	return render_template('producer/preg.html', title="Producer Register", form=form)

@producer.route('/logout')
def logout():
	session['p_uname'] = None
	session['p_pass'] = None
	return redirect(url_for('producer.login'))
	
@producer.route('/qrviewer/<qkey>')
def qrviewer(qkey):
	return render_template('producer/qr.html', qr=qr.qrcode(qkey))