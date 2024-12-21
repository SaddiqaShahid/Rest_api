FastAPI Item Management API

It is a  FastAPI project that allows you to manage a list of items. You can add and delete  items to list  through API endpoints.

Features
1. Add Items:
Add items to list.

3. Delete Items:
Remove items from the list.


Endpoints

POST /item

o  item (string): The name of the item to add.

o  Response: Returns the updated list of items.

DELETE /items/{item_name}

o  item_name (string): The name of the item to delete.

o  Response: Returs updated list of items.
