#Database Layer
from datetime import datetime
from flask import current_app
from TrashTagBackend import db
import string
import random as rnd

#https://pypi.org/project/flask-googlemaps/

disposer_product_association = db.Table(
	'DisposerProductAssociations',
	db.Column('disposer_id', db.Integer, db.ForeignKey('user_model.id')),
	db.Column('product_id', db.Integer, db.ForeignKey('product.id')),
)

dustbin_product_association = db.Table(
	'DustbinProductAssociations',
	db.Column('dustbin_id', db.Integer, db.ForeignKey('dustbin.id')),
	db.Column('product_id', db.Integer, db.ForeignKey('product.id')),
)


cset = string.ascii_uppercase+string.ascii_lowercase+string.digits

class LocationModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	lat = db.Column(db.Float)
	lng = db.Column(db.Float)
	name = db.Column(db.String) #Nickname for Location
	dustbins = db.relationship('Dustbin', backref='location')

	def __init__(self, name, latitude, longitude):
		self.lat = latitude
		self.lng = longitude
		self.name = name

	def __repr__(self):
		return f"Location({self.name}->({self.lat},{self.lng})"

class UserModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	username = db.Column(db.String)
	password = db.Column(db.String)
	coins = db.Column(db.Integer, default=0)

	disposed_products = db.relationship('Product', secondary=disposer_product_association, 
		backref=db.backref('disposers', lazy='dynamic'))


	def __init__(self, uname, pwd, name):
		self.name = name
		self.username = uname
		self.password = pwd

	def __repr__(self):
		return f"User({self.username})"

class DistributorModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String) #Name
	distributorkey = db.Column(db.String) #CustomStringKey
	dustbins = db.relationship('Dustbin', backref='distributor')

	username = db.Column(db.String)
	password = db.Column(db.String)

	def __init__(self, name, uname, pwd):
		cset = string.ascii_uppercase+string.ascii_lowercase+string.digits
		self.name = name
		self.username = uname
		self.password = pwd
		self.distributorkey = ''.join([rnd.choice(cset) for _ in range(10)])


	def __repr__(self):
		return f"Distributor({self.name})"

class ProducerModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String) #Name
	producerkey = db.Column(db.String) #CustomStringKey
	products = db.relationship('Product', backref='producer')

	username = db.Column(db.String)
	password = db.Column(db.String)

	def __init__(self, name, uname, pwd):
		self.name = name
		self.username = uname
		self.password = pwd
		self.producerkey = ''.join([rnd.choice(cset) for _ in range(10)])

	def __repr__(self):
		return f"Producer({self.name})"

class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	is_biodegradable = db.Column(db.String)
	waste_type = db.Column(db.String) #Dry/Wet/Recycleable Waste
	productkey = db.Column(db.String)

	producer_id = db.Column(db.Integer, db.ForeignKey('producer_model.id'))


	def __init__(self, name, isbiodegradable, waste_type, producer):
		self.name = name
		self.is_biodegradable = isbiodegradable
		self.productkey = ''.join([rnd.choice(cset) for _ in range(10)])
		self.waste_type = waste_type
		producer.products.append(self)

	def add2dustbin(self, disposer, dustbin):
		disposer.disposed_products.append(self)
		dustbin.contents.append(self)
		disposer.coins += 10
		db.session.commit()

	@property
	def is_disposed(self):
		return (self in self.dustbins)

	def __repr__(self):
		return f"Product({self.name}, {self.producer})"

class Dustbin(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	dustbinkey = db.Column(db.String)
	dustbin_type = db.Column(db.String)#Corresponds to Product.waste_type
	location_id = db.Column(db.Integer, db.ForeignKey('location_model.id'))
	distributor_id = db.Column(db.Integer, db.ForeignKey('distributor_model.id'))
	contents = db.relationship('Product', secondary=dustbin_product_association, 
				backref=db.backref('dustbins', lazy='dynamic'))
	
	def __init__(self, name, dustbin_type, location, distributor):
		self.name = name
		self.dustbinkey = ''.join([rnd.choice(cset) for _ in range(10)])
		self.dustbin_type = dustbin_type
		location.dustbins.append(self)
		distributor.dustbins.append(self)

	def __repr__(self):
		return f"Dustbin({self.name}, {self.distributor}, {self.dustbin_type})"