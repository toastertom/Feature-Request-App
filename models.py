from datetime import datetime

from sqlalchemy import desc

from formSrvc import db

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(1500), nullable=False)
    target = db.Column(db.Text, nullable=True)
    client = db.Column(db.Text, nullable=True)
    category = db.Column(db.Text, nullable=True)
    rank = db.Column(db.Integer, nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

# This needs to be added to a different file.
    # @staticmethod
    # def sort_by_priority():
    #     return Request.query.order_by(desc(Request.rank))
    #
    def __repr__(self):
        return "<Request '{}': '{}'>".format(self.description, self.title)
