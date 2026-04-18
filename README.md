# Task Tracker CLI

A simple command-line task manager built using Python.

---

## Features
- Add, update, delete tasks
- Mark tasks as done or in-progress
- Filter tasks by status
- JSON-based storage
- No external libraries used

---

## Architecture Diagram

<img width="1024" height="1400" alt="image" src="https://github.com/user-attachments/assets/dbd3927f-ac33-478c-a0b0-265a4fe76285" />

---

## Installation

```bash
git clone https://github.com/your-username/task-tracker-cli.git
cd task-tracker-cli
```

## Usage

Add a task
```
task add "Finish assignment"
```
List tasks
```
task list
```
Filter tasks
```
task list done
task list todo
task list in-progress
```
Update a task
```
task update 1 "Finish math assignment"
```
Delete a task
```
task delete 1
```
Mark status
```
task mark-done 1
task mark-in-progress 1
```

## Commands

| Command          | Description         |
| ---------------- | ------------------- |
| add              | Add a task          |
| update           | Update a task       |
| delete           | Delete a task       |
| mark-done        | Mark as done        |
| mark-in-progress | Mark as in progress |
| list             | Show tasks          |

## Tech Stack
-Python
-JSON
-CLI

## Future Improvements
-Priority levels
-Due dates
-Search functionality


---

# ⚙️ Git Commands (DO THIS)

```bash
git init
git add .
git commit -m "Initial commit - Task Tracker CLI"
git branch -M main
git remote add origin https://github.com/your-username/task-tracker-cli.git
git push -u origin main
```
