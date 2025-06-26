from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

List_of_todo_items = ["write","read", "code", "test"]


@app.route('/todo', methods=['GET'])
def get_todo_items():
    return {'todo_items': List_of_todo_items}


@app.route('/todo', methods=['POST'])
def add_todo_item():
    new_item = request.json.get('item')  
    List_of_todo_items.append(new_item)
    return {'todo_items': List_of_todo_items}


@app.route('/todo/delete/<int:item_id>', methods=['DELETE'])
def delete_todo_items(item_id):
    if 0 <= item_id < len(List_of_todo_items):
        deleted_item = List_of_todo_items.pop(item_id)
        return {'message': f'Item "{deleted_item}" deleted successfully.', 'todo_items': List_of_todo_items}
    else:
        return {'error': 'Invalid item ID'}
    
    
@app.route('/todo/update/<int:item_id>', methods=['PUT'])
def update_todo_item(item_id):
    if 0 <= item_id < len(List_of_todo_items):
        updated_item = request.json.get('item')
        List_of_todo_items[item_id] = updated_item
        return {'message': f'Item updated to "{updated_item}".', 'todo_items': List_of_todo_items}
    else:
        return {'error': 'Invalid item ID'}