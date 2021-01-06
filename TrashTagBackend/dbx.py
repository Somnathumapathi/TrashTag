from TrashTagBackend import create_app, db
app = create_app()
ac = app.app_context()
from TrashTagBackend.models import LocationModel, Dustbin, Product, ProducerModel, DistributorModel

with ac:
	#Locations
	# l1 = LocationModel('Imversion', 12.943824027778026, 77.58483989525608)
	# l2 = LocationModel('MyCaptain', 12.917735223808648, 77.6267522971101)
	# l3 = LocationModel('Dominos', 12.923758407570853, 77.64662205737554)
	# l4 = LocationModel('AmpleMart', 12.925206448921639, 77.5883182222381)
	# db.session.add(l1)
	# db.session.add(l2)
	# db.session.add(l3)
	# db.session.add(l4)
	# db.session.commit()