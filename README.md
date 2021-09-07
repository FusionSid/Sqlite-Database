# Sqlite Database

This is a database made with sqlite3 that stores people. It stores their firstnames, lastname and age and generates an id for them. Then it jsonify's the content of the database and puts it up on a flask website. This can be used with the request module to send requests to the website and get the json data of the people. 

### Usage
To make a person example:
```p = Person("Firstname", "Lastname", 42)```
This uses the the person class ^.

Then run: ```insert_per(p)``` to insert this new person into the database.

There are more commands and all of them can be found in the database.py file.
### Website
The homepage of the flask website returns all the people in the database.
#### How to get specific answers from the website:
To get specific answers change the url of the site.
The homepage will be /. If you want to search by firstname, change the url to /first=<Firstname> and same for lastname,age and id.

This projects is really just a test and I might use this database/flask knowledge to make something usefull unlike this person api in the future
