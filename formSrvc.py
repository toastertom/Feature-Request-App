import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# import models
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'requests.db')
# db Represents the database connection.
db = SQLAlchemy(app)

import models

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/postservice', methods=['POST'])
def postservice():
    title = request.form['title']
    description = request.form['description']
    target = request.form['target']
    client = request.form['client']
    category = request.form['category']
    rank = request.form['rank']
    # Database
    req = models.Request(title=title, description=description, target=target, client=client, category=category, rank=rank)
    db.session.add(req)
    db.session.commit()

    return jsonify({'title' : title, 'description' : description, 'target' : target, 'client' : client, 'category' : category, 'rank' : rank})

if __name__ == '__main__':
    app.run(debug=True)
