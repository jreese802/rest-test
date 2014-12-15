#!flask/bin/python
from flask import Flask, jsonify, abort, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    },
    {
        'id': 3,
        'title': u'Do things.',
        'description': u'Need to do things.', 
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
  task = filter(lambda t: t['id'] == task_id, tasks)
  if len(task) == 0:
      abort(404)
  # my_response = map(jsonify,task)
  return jsonify(task[0])

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
  if not request.form or not 'title' in request.form:
      abort(400)
  task = {
      'id': tasks[-1]['id'] + 1,
      'title': request.form['title'],
      'description': request.form['description'],
      'done': False
  }
  tasks.append(task)
  return jsonify({'task': task}), 201

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
  task = get_task_by_id(task_id)
  if len(task) == 0:
      abort(404)
  if request['description']:
    get_task_by_id(task_id)['description'] = request['description']
  if request['title']:
    get_task_by_id(task_id)['title'] = request['title']
  if request['done']:
    get_task_by_id(task_id)['done'] = request['done']
  return jsonify({'task': get_task_by_id(task_id)}), 201

@app.route('/todo/api/v1.0/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
  task = get_task_by_id(task_id)
  if len(task) == 0:
      abort(404)
  else:
    tasks.remove(get_task_by_id(task_id))
  return jsonify({'tasks':tasks}), 201

def get_task_by_id(task_id):
  return filter(lambda t: t['id'] == task_id, tasks)

if __name__ == '__main__':
    app.run(debug=True)
