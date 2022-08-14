# AirBnB clone - The console

## The Overview:
It is the first part of the whole of (AirBnB clone: Web Application) project. This first step, is necessary, entails building a minified console (like a shell) to manage the underlying data structure for the whole project in a sense of data flow and communication with **HTML/CSS templating**, **database storage**, **API**, **front-end integration** etc, which are other parts of whole project.  
## The Console in Action:
It is like other **CLI Programs** but ours is limited to a specific use-case. With this **HBNB** console, we should be able to manage the objects of our project through operations similar to **CRUD** operations:
* Create a new object (ex: a new User or a new Place).
* Retrieve an object from a file, a database (from a storage mean).
* Update attribute of an object.
* Destroy an object.
* Do operations like counting, reading time of new entry of an object, etc.  

**To Use HBNB Console:**  
* Through CLI program (Git bash, powershell, etc), run **python (or py) console.py** - windows operating system.  
Or **./console.py** - for Linux Distribution.
* When become activated, you should see a prompt like this:  
**(hbnb)**
* type **help** in the prompt to see the supported commands at a glance.
* type **help command_name** to learn what such command does.  

**Example:**  
* **./console.py**
* **(hbnb) help**  
Documented commands (type help <topic>):  
============================   
EOF help quit all create show update destroy  

* **(hbnb)** help create  
```
	create command creates a new instance of supported
	class name pass as parameter to create command. ex:
	create BaseModel
	And save the instance to storage file.
```
