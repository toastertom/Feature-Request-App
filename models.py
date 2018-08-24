from datetime import datetime

from sqlalchemy import desc

from app import db, ma

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(1500), nullable=False)
    target = db.Column(db.Text, nullable=True)
    client = db.Column(db.Text, nullable=True)
    category = db.Column(db.Text, nullable=True)
    rank = db.Column(db.Integer, nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    @staticmethod
    def sort_by_rank():
        return Request.query.order_by(Request.rank)

# RequestSchema is telling Marshmallow how to structure the data conversion to JSON.
class RequestSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'target', 'client', 'category', 'rank', 'date')

request_schema = RequestSchema(many=True, strict=True)
print(request_schema)
