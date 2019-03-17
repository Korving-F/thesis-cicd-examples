from flask import Flask
from flask_restful import reqparse, abort, Api, Resource


TODOS = {
    'todo1': {'task': 'Analyize various CI tools'},
    'todo2': {'task': 'Compare them and make a pick'},
    'todo3': {'task': 'Expand pipelines for Certidude'},
}

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201


class App():
    def __init__(self):
        self.app = Flask(__name__)
        api = Api(self.app)
        api.add_resource(TodoList, '/todos')
        api.add_resource(Todo, '/todos/<todo_id>')


    def run(self, host='0.0.0.0', port='80', debug=True):
        self.app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    app = App()
    app.run()
