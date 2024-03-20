from flask import request
import uuid
from db import items
from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import ItemSchema

blp = Blueprint("items", __name__, description='Operations on items')


@blp.route('/item')
class Item(MethodView):
    def get(self):
        id = request.args.get("id")
        if id is None:
            return {"items": items}
        try:
            return items[id]
        except KeyError:
            return {'message': 'record not found'}, 400
        
        
        
    @blp.arguments(ItemSchema)
    def post(self,request_data):
        new_id = uuid.uuid4().hex
        items[new_id] = request_data
        return {"msg": "item is added successfully"}, 201
    
    
    @blp.arguments(ItemSchema)
    def put(self,request_data):
        id = request.args.get("id")
        if id is None:
            return {"msg": "given id not found"}, 400

        if id in items.keys():
            items[id] = request_data
            return {"msg": "item is updated successfully"}
        return {'message': 'record not found'}, 400

    def delete(self):
        id = request.args.get("id")
        if id is None:
            return {"msg": "given id not found"}, 400

        if id in items.keys():
            del items[id]
            return {"msg": "item is deleted successfully"}
        return {'message': 'record not found'}, 400
