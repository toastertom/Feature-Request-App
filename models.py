from datetime import datetime

from sqlalchemy import desc

from formSrvc import db, ma

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
    # def sort_by_rank():
    #     return Request.query.order_by(desc(Request.rank))
    #
    # @staticmethod
    # def get_all_requests():
    #     return Request.query.all()

    # def __init__(self, id, title, description, target, client, category, rank, date):
    #     self.id = id
    #     self.title = title
    #     self.description = description
    #     self.target = target
    #     self.client = client
    #     self.category = category
    #     self.rank = rank
    #     self.date = date
        # self.id = data.get('id'),
        # self.title = data.get('title'),
        # self.description = data.get('description'),
        # self.target = data.get('target'),
        # self.client = data.get('client'),
        # self.category = data.get('category'),
        # self.rank = data.get('rank'),
        # self.date = data.get('date')
            # 'title' : self.title,
            # 'description' : self.description,
            # 'target' : self.target,
            # 'client' : self.client,
            # 'category' : self.category,
            # 'rank' : self.rank,
            # 'date' : self.date

        # return "<Request id : '{}', title: '{}', description: '{}', target: '{}', client: '{}', category: '{}', rank: '{}', date: '{}' >".format(self.id, self.title, self.description, self.target, self.client, self.category, self.rank, self.date)

class RequestSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'target', 'client', 'category', 'rank', 'date')

request_schema = RequestSchema(many=True, strict=True)
print(request_schema)
# requests_schema = request_schema(many=True)
