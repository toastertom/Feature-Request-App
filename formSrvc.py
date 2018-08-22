from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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

    return jsonify({'title' : title, 'description' : description, 'target' : target, 'client' : client, 'category' : category, 'rank' : rank})

if __name__ == '__main__':
    app.run(debug=True)
