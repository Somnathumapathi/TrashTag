#Database Layer
from datetime import datetime
from flask import current_app
from TrashTagBackend import db

#https://pypi.org/project/flask-googlemaps/


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


class DistributorModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String) #Name
	distributorkey = db.Column(db.String) #CustomStringKey
	dustbins = db.relationship('Dustbin', backref='distributor')

	def __init__(self, name):
		self.name = name
		self.distributorkey = distributorkey

	def __repr__(self):
		return f"Distributor({self.name})"

class ProducerModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String) #Name
	producerkey = db.Column(db.String) #CustomStringKey
	products = db.relationship('Product', backref='producer')

	def __init__(self, name):
		self.name = name
		self.producerkey = producerkey

	def __repr__(self):
		return f"Producer({self.name})"

class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	is_biodegradable = db.Column(db.String)
	waste_type = db.Column(db.String) #Dry/Wet/Recycleable Waste
	productkey = db.Column(db.String)

	producer_id = db.Column(db.Integer, db.ForeignKey('producer_model.id'))
	dustbin_id = db.Column(db.Integer, db.ForeignKey('dustbin.id'))

	def __init__(self, name, isbiodegradable, productkey, waste_type, prod):
		self.name = name
		self.is_biodegradable = isbiodegradable
		self.productkey = productkey
		self.waste_type = waste_type
		prod.products.append(self)

	def __repr__(self):
		return f"Product({self.name}, {self.owner})"

class Dustbin(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	dustbinkey = db.Column(db.String)
	dustbin_type = db.Column(db.String)#Corresponds to Product.waste_type
	location_id = db.Column(db.Integer, db.ForeignKey('location_model.id'))
	distributor_id = db.Column(db.Integer, db.ForeignKey('distributor_model.id'))
	contents = db.relationship('Product', backref='dustbin')
	
	def __init__(self, name, dustbinkey, dustbin_type, location):
		self.name = name
		self.dustbinkey = dustbinkey
		self.dustbin_type = dustbin_type
		location.dustbins.append(self)

	def __repr__(self):
		return f"Dustbin({self.name}, {self.owner}, {self.dustbin_type})"