from app import db


class Sale(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    date = db.Column(db.Integer, nullable=False)
    quantity_in_stock= db.Column(db.Integer)
    price = db.Column(db.Float, nullable = False)

    def serialize(self):
        return {
            'id' : self.id,
            'date' : self.date,            
            'quantity_in_stock' : self.quantity_in_stock,
            'price': self.price
        }

