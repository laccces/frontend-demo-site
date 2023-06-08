from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'  # Update with your database path
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api', methods=['GET'])
def get_data():
    data = {'message': 'Hello, World!'}
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
