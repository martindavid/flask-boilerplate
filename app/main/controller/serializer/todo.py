from flask_restplus import Namespace, fields

api = Namespace('Todo', path="/todo",
                description="All related operation for Todo endpoint")


todo = api.model('todo', {
    'message': fields.String(description="Message in todo")
})