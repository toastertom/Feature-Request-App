import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify
from sqlalchemy import desc
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# Sets a path to the current directory.
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'requests.db')
# db Represents the database connection.
db = SQLAlchemy(app)
ma = Marshmallow(app)

import models

@app.route('/')
def index():
    return render_template('index.html')
# Post Request
@app.route('/postservice', methods=['POST'])
def postservice():
    title = request.form['title']
    description = request.form['description']
    target = request.form['target']
    client = request.form['client']
    category = request.form['category']
    rank = request.form['rank']
    # Database
    # req is creating a new constructor object based off the Request Class.
    req = models.Request(title=title, description=description, target=target, client=client, category=category, rank=rank)
    # Adds req to the database session.
    db.session.add(req)
    # Runs the SQL INSERT statement which adds the data to the database.
    db.session.commit()

    return 'post successful'
    # return jsonify({'title' : title, 'description' : description, 'target' : target, 'client' : client, 'category' : category, 'rank' : rank})

# Get Request
@app.route('/getservice', methods=['GET'])
def getservice():
    # all_requests = models.Request.query.all()
    all_requests = models.Request.sort_by_rank()
    results = models.request_schema.dump(all_requests)
    return jsonify(results.data)


if __name__ == '__main__':
    app.run(debug=True)
