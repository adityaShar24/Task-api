from flask import Blueprint , request , make_response
from database import  task_collections , users_collections
import bson.json_util as json_util
import json



task_bp = Blueprint("task_bp",__name__)

@task_bp.post("/tasks")
def Tasks():
    body = json.loads(request.data)
    task = {
        "content": body["content"],
        "completed": False,
        "username": body["username"]
    }
    user = users_collections.find_one({"username": body["username"]})
    if not user:
        return make_response("User not found", 404)

    if task["username"] == user["username"]:
        users_collections.insert_one(task)
    else:
        return make_response("Invalid user", 400)

    
        
    if not task["username"]:
        return make_response("Please mention the userID", 401)

        
    if not task["content"]:
        return make_response("Please enter your tasks" , 401)
        
    saved_tasks = task_collections.insert_one(task).inserted_id
    jsonVersion = json_util.dumps(saved_tasks)
    return {"message": "task added succesully" , "tasks": jsonVersion}


@task_bp.patch("/status")
def Status():
    body = json.loads(request.data)
    content = body["content"]
    task = task_collections.find_one({"content":content})
    update_content = {"content": body["content"]}
    update_result_true = {"$set": {"completed": True}}
    update_result_False = {"$set": {"completed": False}}
    if not task:
        make_response({"message": "Please enter your task"} , 400)
        
    if task["completed"] == True:
        update_task = task_collections.update_one(
            update_content, update_result_False
        )
        return make_response({"meassage":"task is now incomplete"} , 200)
        
    if task["completed"] == False:
        update_task = task_collections.update_one(
            update_content , update_result_False
        )
        return make_response({"meassage":"task is now completed"} , 200)


@task_bp.patch("/edit")
def Edit():
    body = json.loads(request.data)
    content = body["content"]
    task = task_collections.find_one({"content": content})
    update_content = {"content": body["content"]}
    edit_content = {"$set": {"content": body["newcontent"]}}

    task_edit = task_collections.update_one(
        update_content, edit_content
    )
    return make_response("Your task has been edited succesfully", 200)
