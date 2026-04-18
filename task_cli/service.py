import sys
import json
import os
from datetime import datetime
FILE="/Users/vatsalpathak/Task Tracker Project/task_cli/storage.json"
def load_tasks():
    try:
        if not os.path.exist(FILE):
            return []
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        print("Error reading file. Resetting tasks.")
        return []
def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)
def get_next_id(tasks):
    return max([t["id"] for t in tasks], default=0)+1
def add_task(description):
    if not description:
        print("\033[91mError: Description required\033[0m")
        return 
    tasks=load_tasks()
    task={
        "id":get_next_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt":str(datetime.now()),
        "updatedAt":str(datetime.now())
    }
    tasks.append(task)
    save_tasks(tasks)
    print("\033[92mTask added\033[0m")
def list_tasks(filter_status=None):
    tasks=load_tasks()
    if not tasks:
        print("No tasks found.")
        return 
    for t in tasks:
        if filter_status and t["status"] != filter_status:
            continue
        print(f"{t['id']} | {t['description']} | {t['status']}")
def update_task(task_id, new_desc):
    tasks=load_tasks()
    for t in tasks:
        if t['id']==task_id:
            t['description']=new_desc
            t['updatedAt']=str(datetime.now())
            save_tasks(tasks)
            print("Task updated.")
            return
    print("\033[91mTask not found\033[0m")
def delete_task(task_id):
    tasks=load_tasks()
    new_tasks=[t for t in tasks if t['id'] != task_id]
    if len(tasks)==len(new_tasks):
        print("\033[91mTask not found\033[0m")
        return
    save_tasks(new_tasks)
    print("\033[92mTask deleted\033[0m")
def mark_status(task_id, status):
    tasks=load_tasks()
    for t in tasks:
        if t['id']==task_id:
            t['status']=status
            t['updatedAt']=str(datetime.now())
            save_tasks(tasks)
            print(f"Marked as {status}")
            return
    print("\033[91mTask not found\033[0m")
def show_help():
    print("""
Commands:
  add "task"                Add new task
  update <id> "task"        Update task
  delete <id>               Delete task
  mark-done <id>            Mark as done
  mark-in-progress <id>     Mark as in progress
  list                      List all tasks
  list done                 List done tasks
  list todo                 List pending tasks
""")  


