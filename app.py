from flask import Flask, request
import pandas as pd
from random import randint

app = Flask(__name__)

#THIS FUNCTION RETURNS THE ENTIRE DB
@app.route("/")
def home_page():

    #MAIN CSV FILE WHERE ALL DATA IS STORED
    database = pd.read_csv('Task.csv')
    return {"DATABASE":database.to_dict(orient='list')}

#FUNCTION TO CREATE NEW TASKS
@app.route("/create", methods=['POST', 'GET'])
def create_task():
    task = request.args.get('task')
    id = randint(0, 9999) #GENERATE RANDOM ID FOR NEW TASK
    data = pd.DataFrame([[str(id), str(task), '0']]) #CREATE A PANDAS ENTRY OF NEW TASK
    
    try:
        data.to_csv('Task.csv', index=False, mode='a', header=False)
        #UPDATE THE CSV 
    except:
        return {"OUTPUT": "Couldn't Create Task"}
    
    return {"OUTPUT": {"ID": id, "TASK": task, "STATUS": 0}}

#FUNCTION TO UPDATE TASK's STATUS using ID [COMEPLETE/INCOMPLETE]
@app.route("/update")
def update_task():
    id = request.args.get('id')
    status = request.args.get('status')
    # task = request.args.get('task')
    
    try:
        db = pd.read_csv('Task.csv')
        db.loc[db["ID"] == int(id), "STATUS"] = int(status)
        
        db.to_csv('Task.csv', index=False)        
    except:
        return {"OUTPUT": "FAILED"}
    
    return {"OUTPUT": "SUCCESS"}
    

#FUNCTION TO DELETE A TASK using ID
@app.route("/delete")
def del_task():
    id = request.args.get('id')
    
    try:
        db = pd.read_csv('Task.csv')
        db = db.drop(db[db.ID == int(id)].index)
        db.to_csv('Task.csv', index=False)
    except:
        return {"OUTPUT": "FAILED"}
    
    return {"OUTPUT": "SUCCESS"}


#MAIN FUNCTION
if __name__ == '__main__':
    app.run(debug=True)