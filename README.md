FastAPI Item Management API

It is a  FastAPI project that allows you to manage a list of items. You can add and delete  items to list  through API endpoints.

Features
1. Add Items:
Add items to list.

3. Delete Items:
Remove items from the list.


Endpoints

POST /item

item (string): The name of the item to add.
Response: Returns the updated list of items.

DELETE /items/{item_name}

item_name (string): The name of the item to delete.
Response: Returs updated list of items.
