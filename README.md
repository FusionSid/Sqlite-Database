# Sqlite Database

This is a database made with sqlite3 that stores people. It stores their firstnames, lastname and age and generates an id for them. Then it jsonify's the content of the database and puts it up on a flask website. This can be used with the request module to send requests to the website and get the json data of the people. 
To make a person example:
```p = Person("Firstname", "Lastname", 42)```
You can use the person class to do this ^.
Then run: ```insert_per(p)``` to insert this new person into the database.
This projects is really just a test and i might use this database/flask knowledge to make something usefull unlike this person api in the future
