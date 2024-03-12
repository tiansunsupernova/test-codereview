from flask import Flask, jsonify, request
app = Flask(__name__)

tasks = [
    {"id": 1, "title": "First Task", "description": "This is the first task"}
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'message': 'Task not found'}), 404
    return jsonify({'task': task})

@app.route('/task', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        return jsonify({'message': 'Missing title'}), 400
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', "")
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'message': 'Task not found'}), 404
    task['title'] = request.json.get('title', task['title'])
    task['description'] = request.json.get('description', task['description'])
    return jsonify({'task': task})

@app.route('/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)