PYTHON VERSION - 3.10.0

*NOTES*
Task.csv will act as a database for the application.
_________________________________________________________________

STEPS TO RUN THE APPLICATION:

SIMPLY OPEN A TERMINAL IN THE DIRECTORY AND RUN THE COMMAND:
"python app.py"

once the app starts, head to this link - http://127.0.0.1:5000/
this is the homepage, it will show the entire database.
-----------------------------------------------------------------

TO CREATE A NEW TASK 

http://127.0.0.1:5000/create?task=[enter value here]

exmple - http://127.0.0.1:5000/create?task=work+on+Templates

-----------------------------------------------------------------

TO UPDATE THE STATUS OF A TASK

Head to homepage[http://127.0.0.1:5000/] and look for the ID of the said task.

Now simply feed that ID to the API url like this -
http://127.0.0.1:5000/update?id=[enter id here]&status=[enter status value here] 

exmple - http://127.0.0.1:5000/update?id=4451&status=0

-----------------------------------------------------------------

TO DELETE A TASK

we have to specify the id of the task.

go to API url - http://127.0.0.1:5000/delete?id=[enter ID here]

exmple - http://127.0.0.1:5000/delete?id=8783

-----------------------------------------------------------------

ALL THE CHANGES WILL BE REFLECTED ON THE HOMEPAGE, REFRESH AFTER PERFORMING ANY UPDATION OR DELETION TO SEE CHANGES
http://127.0.0.1:5000/

![alt text](https://imgur.com/bVOOcjE)
