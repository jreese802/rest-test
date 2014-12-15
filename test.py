#!flask/bin/python
from flask import Flask, jsonify, abort, request

app = Flask(__name__)


people = [
            {'name':'james',
             'age' :22},

            {'name':'john',
             'age' :19}
          ]

@app.route('/api/people', methods=['GET'])
def get_people():
  return jsonify({'people':people})

@app.route('/api/people/<name>', methods=['GET'])
def get_person(name):
  print name
  person = filter(lambda p: p['name'] == name, people)[0]
  print person
  return jsonify(person)

@app.route('/api/people', methods=['POST'])
def post_person():
  name = request.form['name']
  age = request.form['age']
  new_person = {'name':name,
                'age' :age}
  return jsonify(new_person)

if (__name__) == "__main__":
  app.run(debug=True)