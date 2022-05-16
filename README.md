# Shopify_Tech_Challenge_2023
The project is deployed at the webpage: https://shopifytechchallenge2023.austin6868.repl.co/

## Home Page
The homepage allows users to read a list of the items/inventory located in different warehouses, users are able to push "Go to Item" to examine the name of the item, city, as well as the state the item belongs to.

## Manage Items Page
- Users are able to create, update and delete the existing items. 
- By clicking "Add New" users are able to use the fields to create an item, user would need to input the name of the item, description of the item, the manager of the item, warehouse the item belongs to, the slug (this is a unique string for the system to recogonize the item, usually recommended as the lower case of the item name), and the date created.
- By clickinng "Edit", users are ablt to edit the same fields they or others created.
- By clicking "Delete", users are able to remove a certain item from the database.

## Manage Warehouses Page
- In this page, users are able to create and delete the warehouses.
- By clicking "Add New Warehouse" users could add a warehouse by its name, city, state, size and slug (as mentioned above, would recommend using the lowercase of the warehouse name).
- By clicking "Delete" users are able to remove a certain warehouse from the database.

## Technical Aspects
- This application was built with Django, SQLite as back-end frameworks and Bootstrap as front-end.
- Django provides a robust framwork that ensured the simlicity of the system and enhanced the security of the application.
- SQLite, for the data we are handling in this project, would be sufficient, however it lacks scalability, for the future uses, an implementation of postgreSQL could be implemented to achieve scability.

## Future Features
- Authtntication would be added in the future as the manager number increase.
- Like mentioned before, a more scalable database would be a critical addition as the logistics company would handle hundreds of thousands of orders and inventories per day.
- DBMS scema would also be designed for the scalability and robustness of the data.
