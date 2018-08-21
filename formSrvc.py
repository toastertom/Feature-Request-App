from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/postservice', methods=['POST'])
def postservice():
    title = request.form['title']
    description = request.form['description']
    target = request.form['target']
    client = request.form['client']
    category = request.form['category']
    priority = request.form['priority']

if __name__ == '__main__':
    app.run(debug=True)
