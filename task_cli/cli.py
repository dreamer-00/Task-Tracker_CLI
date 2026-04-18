import sys
from task_cli.service import add_task, delete_task, list_tasks, update_task, mark_status, show_help
def main():
    if len(sys.argv) < 2:
        print("Usage: task <command>")
        return
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
if __name__=="__main__":
    main()