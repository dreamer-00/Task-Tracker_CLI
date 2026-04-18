import sys
import json
import os
from datetime import datetime
FILE="task.json"
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
        print("ERROR: Description Required")
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
    print(f"Task Added (ID: {task['id']})")
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
    print("Task not found.")
def delete_task(task_id):
    tasks=load_tasks()
    new_tasks=[t for t in tasks if t['id'] != task_id]
    if len(tasks)==len(new_tasks):
        print("Task not found.")
        return
    save_tasks(new_tasks)
    print("Task deleted.")
def mark_status(task_id, status):
    tasks=load_tasks()
    for t in tasks:
        if t['id']==task_id:
            t['status']=status
            t['updatedAt']=str(datetime.now())
            save_tasks(tasks)
            print(f"Marked as {status}")
            return
    print("Task not found")
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
if len(sys.argv) < 2:
    show_help()
    sys.exit()
cmd=sys.argv[1]
try:
    if cmd=="add":
        add_task(sys.argv[2])
    elif cmd=="list":
        status=sys.argv[2] if len(sys.argv)>2 else None
        list_tasks(status)
    elif cmd=="update":
        update_task(int(sys.argv[2], sys.argv[3]))
    elif cmd=="delete":
        delete_task(int(sys.argv[2]))
    elif cmd=="mark-done":
        mark_status(int(sys.argv[2]), "done")
    elif cmd=="mark-in-progress":
        mark_status(int(sys.argv[2]), "in-progress")
    else:
        show_help()
except Exception as e:
    print("Error: ", e)

