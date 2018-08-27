#!/usr/bin/python3
"""
    This script accepts an employee ID integer as parameter,
    and then displays on standard output that employee's TODO list progress.

    Output format:
    First Line
        Employee Foo is done with tasks(finished/total)
    Subsequent Lines
        Display the task_title of completed tasks
"""
import requests
from sys import argv


def filter_by_user(datalist, uid):
    """
        filters todos belonging to user
        filters further for completed todos by that user
    """
    total = []
    completed = []
    for todo in datalist:
        if todo.get("userId") == uid:
            total.append(todo)
            if todo.get("completed"):
                completed.append(todo)
    return ({"total": total, "completed":  completed})


if len(argv) == 1:
    uid = 1
else:
    uid = int(argv[1])
todo_url = "https://jsonplaceholder.typicode.com/todos"
user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
    uid
)

todos = requests.get(todo_url)
if todos.status_code != 200:
    print("error: {}".format(todos.status_code))
    exit(0)
user_resp = requests.get(user_url)
if user_resp.status_code != 200:
    print("error: {}".format(user_resp.status_code))
    exit(0)

user = user_resp.json()
todolist = todos.json()
res = filter_by_user(todolist, uid)
print("Employee {} is done with tasks({}/{})".format(
    user.get("name"), len(res.get("completed")),
    len(res.get("total"))
))
for todo in res.get("completed"):
    print("\t {}".format(todo.get("title")))
