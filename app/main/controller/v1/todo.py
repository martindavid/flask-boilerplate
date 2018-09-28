from flask_restplus import Resource
from http import HTTPStatus
from app.main.controller.serializer.todo import api, todo


@api.route('')
class TodoListController(Resource):

    @api.marshal_list_with(todo)
    def get(self):
        return [], HTTPStatus.OK

    @api.expect(todo, skip_none=True)
    @api.response(HTTPStatus.CREATED, 'Todo successfully created')
    def post(self):
        data = dict(api.payload)
        return {}, HTTPStatus.CREATED


@api.route('/<todo_id>')
@api.param('todo_id', 'Todo identifier')
@api.response(HTTPStatus.NOT_FOUND, 'Todo item is not exists')
class TodoController(Resource):

    @api.marshal_with(todo)
    def get(self):
        return {"message": "success"}, HTTPStatus.OK
